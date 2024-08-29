from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.templatetags.static import static
from django.template.defaultfilters import slugify
from django.utils.text import slugify
import uuid


class Post(models.Model):
    """
    This a the model for the blog posts
    related to :model:'auth.User'.

    """

    class PostStatus(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
        )
    blog_image = CloudinaryField('image', default='placeholder')
    body = models.TextField(validators=[MinLengthValidator(100)])
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=PostStatus.choices, default=PostStatus.DRAFT)
    excerpt = models.TextField(max_length=200, blank=True)
    favorites = models.ManyToManyField(
        User, related_name='favorite_posts', blank=True)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']), ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

            if Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{uuid.uuid4().hex[:8]}"

        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    This is the comment also realted
    to :model:'auth.User' with :model:'blog_posts'.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

    def can_modify(self, user):
        return user == self.author


class UserProfile (models.Model):
    """
    Stores user profile data also realted
    to :model:'auth.User',
    Including their personal data.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', null=True, blank=True)
    first_name = models.CharField(
        "First Name", max_length=50, null=True, blank=True)
    last_name = models.CharField(
        "Last Name", max_length=50, null=True, blank=True)
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
    """
    This is to update the user profile
    instance when a user is saved.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
