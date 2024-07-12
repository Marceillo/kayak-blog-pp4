from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    class PostStatus(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=PostStatus.choices, default=PostStatus.DRAFT)
    
    
    class Meta:
        ordering = ['-publish']
        indexes = [
        models.Index(fields=['-publish']),
        ]
    

    def __str__(self):
        return self.title
