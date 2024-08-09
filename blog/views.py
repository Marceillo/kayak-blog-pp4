from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Post, UserProfile, Comment
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import UserProfileForm, PostForm, SearchForm, CommentForm 
from django.contrib.auth import logout
from django.contrib import messages
import cloudinary.uploader
import cloudinary


# Views 

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    comment_form = CommentForm()

    if post.status == Post.PostStatus.PUBLISHED:
        return render(request, 'blog/post_kayak_blog.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
    elif post.status == Post.PostStatus.DRAFT and request.user.is_authenticated and request.user == post.author:
        return render(request, 'blog/post_kayak_blog.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
    else:
        raise Http404("Post not found")
            

def home(request):
    posts = Post.objects.filter(status=Post.PostStatus.PUBLISHED).order_by('-publish')
    return render(request,'blog/index.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')


def kayak_search_result(request):
    form = SearchForm(request.GET)
    results = Post.objects.none()
    query = ''

    if form.is_valid():
        query = form.cleaned_data['q']
        if query:
            results = Post.objects.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(excerpt__icontains=query) |
                Q(author__username__icontains=query) 
        ).filter(status=Post.PostStatus.PUBLISHED).distinct().order_by('-publish')

       
    paginator = Paginator(results, 10 )
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'form': form,
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'blog/kayak_search_result.html', context) 


class Create_Kayak_Post_View(LoginRequiredMixin, CreateView):
    model = Post
    form_class=PostForm
    template_name = 'blog/create_kayak_post.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.cleaned_data.get('delete_image') and self.object.blog_image:
            cloudinary.uploader.destroy(self.object.blog_image.public_id)
            self.object.blog_image = None
        return super().form_valid(form)


#Update posts
class Update_Kayak_Post_View(LoginRequiredMixin, UpdateView):
    model = Post
    form_class=PostForm
    template_name = 'blog/update_kayak_post.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.cleaned_data.get('delete_image') and self.object.blog_image:
            cloudinary.uploader.destroy(self.object.blog_image.public_id)
            self.object.blog_image = None
        return super().form_valid(form)


#Delete posts 
class Delete_Kayak_Post_View(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_kayak_post.html'
    success_url = reverse_lazy('home')


    def get_queryset(self):
        return Post.objects.filter(author=self.request.user) 

#User tobe able to see there posts 
class My_Post_List_View(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/my_post_list.html'
    context_object_name = 'posts'


    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created')

# After login code 
@login_required
def userprofile(request):
    profile,created = UserProfile.objects.get_or_create(user=request.user)
    context = {
        'user': request.user,
        'profile': profile
    }
    return render(request, 'blog/user_profile.html', context)


@login_required
def profile_edit(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'email' in form.cleaned_data:
                request.user.email = form.cleaned_data['email']
                request.user.save()
            profile.save()
            messages.success(request, "Profile updated successfully")
            return redirect('user_profile')
    
    else:
        form = UserProfileForm(instance=profile, user=request.user)

    return render (request, 'blog/profile_edit.html', {'form': form, 'profile':profile})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request,'Your profile has been deleted successfully')
        return redirect('home')
            
    return render(request, 'account/delete_profile.html')


@login_required
def delete_profile_picture(request):
    
        profile = UserProfile.objects.get(user=request.user)

        if profile.profile_picture:

            cloudinary.uploader.destroy(profile.profile_picture.public_id)
            profile.profile_picture = None
            profile.save()
            messages.success(request, "Profile picture deleted successfully")

            
        return redirect('profile_edit')


@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if not comment.can_modify(request.user):
        return HttpResponseForbidden("You can't edit this comment")
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been successfully updated.')
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
        return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment })


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if not comment.can_modify(request.user):
        return HttpResponseForbidden("You can't delete this comment")
    
    if request.method == 'POST':
        post_slug = comment.post.slug
        comment.delete()
        messages.success(request, 'Your comment has been deleted successfully.')
        return redirect('post_detail', slug=post_slug)
  

    return render(request, 'blog/delete_comment.html', {'comment': comment})

    



#the below was to for after password change but did not work
#class BlogPasswordChangeView(PasswordChangeView):
#    template_name = 'account/password_change.html'
#    success_url = reverse_lazy('home')
    
#    def get_success_url(self):
#        return self.success_url
    

