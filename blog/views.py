from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, UserProfile
from .forms import UserProfileForm


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
