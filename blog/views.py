from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, UserProfile
from .forms import UserProfileForm
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView 


# Create your views here.

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
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    
    else:
        form = UserProfileForm(instance=profile)

    return render (request, 'blog/profile_edit.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request,'Your profile has been deleted successfully')
        return redirect('home')
            
    return render(request, 'account/delete_profile.html')


class BlogPasswordChangeView(PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('home')
    
    def get_success_url(self):
        return self.success_url
    

    
