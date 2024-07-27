from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.templatetags.static import static

# Create your models here.

class Post(models.Model):
    class PostStatus(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    blog_image= CloudinaryField('image', default='placeholder')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=PostStatus.choices, default=PostStatus.DRAFT)
    excerpt = models.TextField(max_length=200, blank=True)
    favorites = models.ManyToManyField(User, related_name='favorite_posts', blank=True)
    
    class Meta:
        ordering = ['-publish']
        indexes = [
        models.Index(fields=['-publish']),
        ]
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.pk and not self.blog_image:
            self.blog_image = None
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created'] 
    

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class UserProfile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', null=True, blank=True)
    first_name = models.CharField("First Name",max_length=50, null=True, blank=True)
    last_name =  models.CharField("Last Name",max_length=50, null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    experience_level = models.CharField(max_length=20, blank=True)
    favorite_gear = models.TextField(blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def get_profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return static('images/default_profile_picture.png')

    def __str__(self):
        return f"{self.user.username} Profile"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()    
