from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import Http404, HttpResponseForbidden
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


#General views

"""
List of published blog posts, ordered publish date in decending.
Displaying the posts on the  homepage.
posts filtered by status and publish date.
**Template:**
blog/index.html
""" 
def home(request):
    posts = Post.objects.filter(status=Post.PostStatus.PUBLISHED).order_by('-publish')
    return render(request,'blog/index.html', {'posts': posts})

"""
Return About page, providing information.
**Template:**
blog/about.html
""" 
def about(request):
    return render(request, 'blog/about.html')

"""
Retrieves and displays a blog post by its slug. Raises a 404 error if not found.
Handles comments and favorites linked to the post.

**Context**:
post: An instance of :model:`blog.Post`.
comments: A queryset of :model:`blog.Comment` instances.
comment_form: An instance of :form:`blog.CommentForm`.
is_favorited: Boolean indicating if the post is favorited by the user.
comment_count: Total number of comments on the post.

**Template**:
:template:`blog/post_kayak_blog.html`

**URL Parameters**:
slug: The slug of the post to display.

**Returns**:
A rendered HTML page with post details and comments.
"""
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    comment_form = CommentForm()
    is_favorited = post.favorites.filter(id=request.user.id).exists() if request.user.is_authenticated else False

    comment_count = comments.count()
    
    if post.status == Post.PostStatus.PUBLISHED:
        return render(request, 'blog/post_kayak_blog.html', {
            'post': post, 
            'comments': comments,
            'comment_form': comment_form,
            'is_favorited': is_favorited,
            'comment_count': comment_count

            })
    elif post.status == Post.PostStatus.DRAFT and request.user.is_authenticated and request.user == post.author:
        return render(request, 'blog/post_kayak_blog.html', {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'is_favorited': is_favorited,
            'comment_count': comment_count
            })
    else:
        raise Http404("Post not found")
            
#post views
"""
Creates a new blog post using a form and redirects to the home page.
Handles image deletion or addition to Cloudinary. Displays success or error messages.

**Template**:
template:`blog/create_kayak_post.html`

**Success Message**:
"Your blog post has been successfully created!"

**Error Message**:
"There was an error creating your blog post."
"""
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
        response = super().form_valid(form)

        messages.success(self.request, 'Your blog post has been successfully created!')

        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'There was an error creating your blog post.')
        return super().form_invalid(form)        

"""
Allows a logged-in user to update their own blog post using a form.

 **Template**:
 :template:`blog/update_kayak_post.html`

**Functionality**:
- The `get_queryset` method restricts updates to posts authored by the logged-in user.
- The `form_valid` method sets the current user as the author, deletes the image from cloud storage if requested, 
  and displays a success message upon valid submission.
- The `form_invalid` method shows an error message if the form submission fails.

**Success Message**:
"Your blog post has been successfully updated!"

 **Error Message**:
"There was an error updating your blog post."
"""
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
        response = super().form_valid(form)
           
        messages.success(self.request, 'Your blog post has been successfully updated!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error updating your blog post.')
        return super().form_invalid(form)  


"""
Allows a logged-in user to delete their own blog post.

**Template**:
:template:`blog/delete_kayak_post.html`

 **Functionality**:
- The `get_queryset` method restricts deletions to posts authored by the logged-in user.
- The `form_valid` method displays a success message upon successful deletion.
- The `form_invalid` method shows an error message if there is an issue with deletion.

 **Success Message**:
"The blog post has been deleted successfully."

**Error Message**:
"There was an error deleting this blog post."
"""
class Delete_Kayak_Post_View(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_kayak_post.html'
    success_url = reverse_lazy('home')


    def get_queryset(self):

        return Post.objects.filter(author=self.request.user)
        

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "The blog post has been deleted successfully")

        return super().form_valid(request, *args, **kwargs)
    
    def form_invalid(self, request, *args, **kwargs):
        messages.error(self.request, 'There was an error deleting this blog post.')
        return super().form_invalid(form)  
    
 


"""
This view allows a logged-in user to see a list of their own blog posts.
It uses the Post model and renders a list of posts using the 
blog/my_post_list.html' template. The context object name for the 
posts in the template is 'posts'.

- The `get_queryset` method restricts the displayed posts to those 
authored by the logged-in user, ordered by the most recent creation date.
""" 
class My_Post_List_View(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/my_post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created')



"""
Allows a logged-in user to view a list of their own blog posts.

**Template**:
template:`blog/my_post_list.html`

**Context**:
posts: A queryset of the user's blog posts, ordered by the most recent creation date.

**Functionality**:
The `get_queryset` method restricts displayed posts to those authored by the logged-in user.
""" 
@login_required
def userprofile(request):
    profile,created = UserProfile.objects.get_or_create(user=request.user)
    context = {
        'user': request.user,
        'profile': profile
    }
    return render(request, 'blog/user_profile.html', context)

"""
Allows a logged-in user to edit their profile.

**Functionality**:
 Retrieves or creates a `UserProfile` instance for the logged-in user.
- Handles both GET and POST requests to display and update the profile.

**POST Request**:
- Validates the submitted form data.
- Updates the user's email if provided.
- Displays a success message upon successful update.
- Displays an error message if the form is invalid.

 **GET Request**:
- Renders the profile edit form pre-filled with the user's current profile data.

**Context**:
form: An instance of `UserProfileForm` for editing the profile.
profile: The user's `UserProfile` instance.
"""
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
            message.error(request, "Error updating profile.")

    else:
        form = UserProfileForm(instance=profile, user=request.user)

    return render (request, 'blog/profile_edit.html', {'form': form, 'profile':profile})

"""

"""
@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user

        try:
            logout(request)
            user.delete()
            messages.success(request,'Your profile has been deleted successfully')

        except Exception as e:
            messages.error(request, f"An error occurred while deleting your profile: {str(e)}")
       
            return redirect('home')
            
    return render(request, 'account/delete_profile.html')

"""
Allows a logged-in user to delete their profile.

 **Functionality**:
- Handles POST requests to delete the user's account.
- Logs out the user after successful deletion.
- Displays a success message upon successful deletion.
- Displays an error message if an exception occurs during deletion.

 **POST Request**:
 - Deletes the user account and logs the user out.

**GET Request**:
 - Renders a confirmation page for profile deletion.

**Context**:
None (no additional context is passed to the template).
"""
@login_required
def delete_profile_picture(request):
    
        profile = UserProfile.objects.get(user=request.user)

        if profile.profile_picture:

            cloudinary.uploader.destroy(profile.profile_picture.public_id)
            profile.profile_picture = None
            profile.save()
            messages.success(request, "Profile picture deleted successfully")
        else:
            messages.error(request, "No profile picture to delete.")

            
        return redirect('profile_edit')

"""
Allows a logged-in user to add a comment to a blog post.

 **Functionality**:
- Retrieves the blog post by its slug.
- Handles POST requests to submit a new comment.
- Displays a success message upon successful addition of the comment.
- Redirects back to the post detail page.

**POST Request**:
- Validates the submitted comment form.
- Associates the comment with the post and the logged-in user.

**GET Request**:
- Redirects to the post detail page without adding a comment.

**Context**:
None (no additional context is passed to the template).
"""
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
            messages.success(request, 'Your comment has been successfully added.')
            return redirect('post_detail', slug=post.slug)
    else:
        messages.error(request, 'Error adding your comment.')
        # form = CommentForm()
    return redirect('post_detail', slug=post.slug)
        

"""
Allows a logged-in user to edit their own comment.

**Functionality**:
 Retrieves the comment by its ID.
- Checks if the user is allowed to modify the comment.
- Handles both GET and POST requests for editing the comment.
- Displays success or error messages based on the form submission.

**POST Request**:
- Validates the submitted comment form.
- Updates the comment with the new data.
- Redirects to the post detail page upon successful update.

 **GET Request**:
- Renders the edit comment form pre-filled with the current comment data.
**Context**:
form: An instance of `CommentForm` for editing the comment.
comment: The `Comment` instance being edited.
"""
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if not comment.can_modify(request.user):
        messages.error(request,"You can't edit this comment.")
        return redirect('post_detail', slug=comment.post.slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been successfully updated.')
            return redirect('post_detail', slug=comment.post.slug)
        else:
            messages.error(request, 'Error editing the your comment.')
    else:
        form = CommentForm(instance=comment)
        return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment })


"""
Allows a logged-in user to delete their own comment.

 **Functionality**:
- Retrieves the comment by its ID.
- Checks if the user is allowed to delete the comment.
- Handles both GET and POST requests for deleting the comment.
- Displays a success message upon successful deletion.

**POST Request**:
- Deletes the comment.
- Redirects to the post detail page after deletion.

 **GET Request**:
 - Renders a confirmation page for comment deletion.

**Context**:
comment: The `Comment` instance being deleted.
"""
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if not comment.can_modify(request.user):
        messages.error(request, "You can't delete this comment")
        return redirect('post_detail', slug=comment.post.slug)
    
    if request.method == 'POST':
        post_slug = comment.post.slug
        comment.delete()
        messages.success(request, 'Your comment has been deleted successfully.')

        return redirect('post_detail', slug=post_slug)
  

    return render(request, 'blog/delete_comment.html', {'comment': comment})

"""
Allows a logged-in user to toggle the favorite status of a blog post.

**Functionality**:
- Retrieves the blog post by its slug.
- Toggles the favorite status of the post for the logged-in user.
- Displays a success message upon successful toggling of the favorite status.
- Displays an error message if an exception occurs during the process.

**POST Request**:
- Adds or removes the user from the post's favorites list.
- Redirects to the post detail page after toggling the favorite status.

 **Context**:
 None (no additional context is passed to the template).
"""
@login_required
def kayak_toggle_favorite(request, slug):
    post = get_object_or_404(Post, slug=slug)
    try:
        if request.user in post.favorites.all():
            post.favorites.remove(request.user)
            messages.success(request, "Blog unfavorited successfully.")
        else:
            post.favorites.add(request.user)
            messages.success(request, "Blog favorited successfully.")

    except Exception as e:
        messages.error(request, 'Error occured while updating your favorite.')    

    return redirect('post_detail', slug=post.slug)


"""
Handles search functionality for blog posts based on user queries.

**Functionality**:
- Retrieves search queries from the GET request using `SearchForm`.
- Filters published blog posts based on the search query across multiple fields.
- Paginates the search results to display a limited number of posts per page.

**GET Request**:
- Validates the search form and retrieves the search query.
- Filters posts by title, body, excerpt, or author username.
 Returns a paginated list of search results.

*Context**:
form: An instance of `SearchForm` for the search input.
page_obj: A paginated object containing the search results.
query: The search query entered by the user.
"""    
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




