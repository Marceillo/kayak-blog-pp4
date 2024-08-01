from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Post, UserProfile
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import UserProfileForm, PostForm
from django.contrib.auth import logout
from django.contrib import messages
import cloudinary.uploader
import cloudinary



#from django.urls import reverse_lazy
#from allauth.account.views import PasswordChangeView 


# Views 

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.status == Post.PostStatus.PUBLISHED:
        return render(request, 'blog/post_kayak_blog.html', {'post': post})
    elif post.status == Post.PostStatus.DRAFT and request.user.is_authenticated and request.user == post.author:
        
            
            return render(request, 'blog/post_kayak_blog.html', {'post: post'})
            
            raise Http404("Post not found")
            

def home(request):
    posts = Post.objects.filter(status=Post.PostStatus.PUBLISHED).order_by('-publish')
    return render(request,'blog/index.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')


def kayak_search_result(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(author__username__icontains=query) 
        ).filter(status=Post.PostStatus.PUBLISHED).distinct().order_by('-publish')
    else:
        results = Post.objects.filter(status=Post.PostStatus.PUBLISHED).order_by('-publish')
    
    paginator = Paginator(results, 10 )
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/kayak_search_result.html', {'page_obj': page_obj, 'query':query}) 


#def kayak_search_result(request):



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





#the below was to for after password change but did not work
#class BlogPasswordChangeView(PasswordChangeView):
#    template_name = 'account/password_change.html'
#    success_url = reverse_lazy('home')
    
#    def get_success_url(self):
#        return self.success_url
    

