from django.contrib import admin
from .models import Post, Comment, UserProfile

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    search_fields = ['title', 'body']
    list_filter = ['status', 'created', 'publish', 'author']
    prepopulated_fields = {'slug': ('title',)}

    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created', ]
    list_filter = ['created']
    search_fields = ['author__username', 'body']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'profile_picture',
        'first_name', 'last_name', 'location', 'experience_level', ]
    list_filter = ['location', 'experience_level']
    search_fields = [
        'user__username', 'first_name',
        'last_name', 'location', 'bio']
    fields = [
        'user', 'profile_picture', 'first_name',
        'last_name', 'location', 'experience_level',
        'favorite_gear', 'bio']
