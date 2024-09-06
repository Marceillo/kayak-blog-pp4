from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q

import cloudinary.uploader
import cloudinary

from .models import Post, UserProfile, Comment
from .forms import UserProfileForm, PostForm, SearchForm, CommentForm

# General views


def home(request):
    """
    Displaying the posts on the homepage.
    blog/index.html template used
    """
    posts = (Post.objects
             .filter(status=Post.PostStatus.PUBLISHED)
             .order_by('-publish'))
    return render(request, 'blog/index.html', {'posts': posts})


def about(request):
    """
    About page display.
    blog/about.htm template used
    """
    return render(request, 'blog/about.html')


def post_detail(request, slug):
    """
    To read the posts in detail and
    creates a url for each post link.
    Comments and favorites feature are linked to the post.
    blog/post_kayak_blog.html template used.
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    comment_form = CommentForm()
    is_favorited = (post.favorites.filter(id=request.user.id).exists()
                    if request.user.is_authenticated
                    else False)
    comment_count = comments.count()

    if post.status == Post.PostStatus.PUBLISHED:
        return render(request, 'blog/post_kayak_blog.html', {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'is_favorited': is_favorited,
            'comment_count': comment_count
        })
    elif (post.status == Post.PostStatus.DRAFT
          and request.user.is_authenticated
          and request.user == post.author):
        return render(request, 'blog/post_kayak_blog.html', {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'is_favorited': is_favorited,
            'comment_count': comment_count
        })
    else:
        raise Http404("Post not found")


class Create_Kayak_Post_View(LoginRequiredMixin, CreateView):
    """
    User are able to create new post using a form.
    blog/create_kayak_post.html used template
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/create_kayak_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.cleaned_data.get('delete_image') and self.object.blog_image:
            cloudinary.uploader.destroy(self.object.blog_image.public_id)
            self.object.blog_image = None
        response = super().form_valid(form)
        messages.success(
            self.request, 'Your blog post has been successfully created!')
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, 'There was an error creating your blog post.')
        return super().form_invalid(form)


class Update_Kayak_Post_View(LoginRequiredMixin, UpdateView):
    """
    Logged in user can update their own blog post using a form.
    blog/update_kayak_post.html template used.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/update_kayak_post.html'
    success_url = reverse_lazy('my_post_list')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.cleaned_data.get('delete_image') and self.object.blog_image:
            cloudinary.uploader.destroy(self.object.blog_image.public_id)
            self.object.blog_image = None
        response = super().form_valid(form)
        messages.success(
            self.request, 'Your blog post has been successfully updated!')
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, 'There was an error updating your blog post.')
        return super().form_invalid(form)


class Delete_Kayak_Post_View(LoginRequiredMixin, DeleteView):
    """
    Enables logged in user to delete their own blog post.
    blog/delete_kayak_post.html template used

    """
    model = Post
    template_name = 'blog/delete_kayak_post.html'
    success_url = reverse_lazy('my_post_list')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(
            self.request, "The blog post has been deleted successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'There was an error deleting this blog post.')
        return super().form_invalid(form)


class My_Post_List_View(LoginRequiredMixin, ListView):
    """
    This view allows a logged in user to see a
    list of their created blog posts.
    blog/my_post_list.html template used.
    """
    model = Post
    template_name = 'blog/my_post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user).order_by('-created')


@login_required
def userprofile(request):
    """
    Allows a logged in user to view their profile.
    blog/user_profile.html template used
    """
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    context = {
        'user': request.user,
        'profile': profile
    }
    return render(request, 'blog/user_profile.html', context)


@login_required
def profile_edit(request):
    """
    Allows a logged in user to edit their
    profile. blog/profile_edit.html template used.
    """
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST,
            request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'email' in form.cleaned_data:
                request.user.email = form.cleaned_data['email']
                request.user.save()
            profile.save()
            messages.success(request, "Profile updated successfully")
            return redirect('user_profile')
        else:
            messages.error(request, "Error updating profile.")
    else:
        form = UserProfileForm(instance=profile, user=request.user)
    return render(
        request,
        'blog/profile_edit.html', {'form': form, 'profile': profile})


@login_required
def delete_profile(request):
    """
    Allows a logged in user to delete their profile.

    """
    if request.method == 'POST':
        user = request.user
        try:
            logout(request)
            user.delete()
            messages.success(
                request,
                'Your profile has been deleted successfully')
            return redirect('home')
        except Exception as e:
            messages.error(
                request,
                f"An error occurred while deleting your profile: {str(e)}")
            return redirect('home')
    return render(request, 'account/delete_profile.html')


@login_required
def delete_profile_picture(request):
    """
    For users to delete their profile picture.
    The picture is also deleted from Cloudinary.
    """
    profile = UserProfile.objects.get(user=request.user)
    if profile.profile_picture:
        cloudinary.uploader.destroy(profile.profile_picture.public_id)
        profile.profile_picture = None
        profile.save()
        messages.success(request, "Profile picture deleted successfully")
    else:
        messages.error(request, "No profile picture to delete.")
    return redirect('profile_edit')


@login_required
def add_comment(request, slug):
    """
    Allows a logged in user to add a comment to a blog post.
    Handles errors and success messages.
    """
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(
                request,
                'Your comment has been successfully added.')
            return redirect('post_detail', slug=post.slug)
    else:
        messages.error(request, 'Error adding your comment.')
    return redirect('post_detail', slug=post.slug)


@login_required
def edit_comment(request, comment_id):
    """
    Allows a logged in user to edit their own comments.
    blog/edit_comment.html template used
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if not comment.can_modify(request.user):
        messages.error(request, "You can't edit this comment.")
        return redirect('post_detail', slug=comment.post.slug)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your comment has been successfully updated.')
            return redirect('post_detail', slug=comment.post.slug)
        else:
            messages.error(request, 'Error editing your comment.')
    else:
        form = CommentForm(instance=comment)
    return render(
        request,
        'blog/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    """
    Allows a logged in user to delete their own comment.
    blog/delete_comment.html template used.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if not comment.can_modify(request.user):
        messages.error(request, "You can't delete this comment")
        return redirect('post_detail', slug=comment.post.slug)
    if request.method == 'POST':
        post_slug = comment.post.slug
        comment.delete()
        messages.success(
            request,
            'Your comment has been deleted successfully.')
        return redirect('post_detail', slug=post_slug)
    return render(request, 'blog/delete_comment.html', {'comment': comment})


@login_required
def kayak_toggle_favorite(request, slug):
    """
    Allows a logged in user to toggle the favorite status of a blog post.

    """
    post = get_object_or_404(Post, slug=slug)
    try:
        if request.user in post.favorites.all():
            post.favorites.remove(request.user)
            messages.success(request, "Blog unfavorited successfully.")
        else:
            post.favorites.add(request.user)
            messages.success(request, "Blog favorited successfully.")
    except Exception as e:
        messages.error(request, 'Error occurred while updating your favorite.')
    return redirect('post_detail', slug=post.slug)


def kayak_search_result(request):
    """
    This is to be able to search
    the title, body, excerpt, and author .
    blog/kayak_search_result.html template used.
    """
    form = SearchForm(request.GET)
    results = Post.objects.none()
    query = ''
    if form.is_valid():
        query = form.cleaned_data['q']
        if query:
            results = (Post.objects
                       .filter(
                           Q(title__icontains=query) |
                           Q(body__icontains=query) |
                           Q(excerpt__icontains=query) |
                           Q(author__username__icontains=query)
                       )
                       .filter(status=Post.PostStatus.PUBLISHED)
                       .distinct()
                       .order_by('-publish'))
    paginator = Paginator(results, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'form': form,
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'blog/kayak_search_result.html', context)
