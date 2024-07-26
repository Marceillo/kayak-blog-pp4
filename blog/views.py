from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, UserProfile
from .forms import UserProfileForm
from django.contrib.auth import logout
from django.contrib import messages
import cloudinary.uploader
import cloudinary



#from django.urls import reverse_lazy
#from allauth.account.views import PasswordChangeView 


# Create your views here.

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.PostStatus.PUBLISHED)
    return render(request, 'blog/post_kayak_blog.html', {'post': post})

def home(request):
    posts = Post.objects.filter(status=Post.PostStatus.PUBLISHED).order_by('-publish')
    return render(request,'blog/index.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')


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
    

