from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, UserProfile


# Create your views here.

def home(request):
    posts = Post.objects.filter(status=Post.PostStatus.PUBLISHED).order_by('-publish')
    return render(request,'blog/index.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html') 

@login_required
def userprofile(request):
    return render(request, 'blog/user_profile.html')
    profile,created = UserProfile.objects.get_or_create(user=request.user)
    context = {
        'user': request.user,
        'profile': profile
    }
    return render (request, 'blog/user_profile.html', context)
