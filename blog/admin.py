from django.contrib import admin
from .models import Post, Comment, UserProfile

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','author','publish','status']
    search_fields = ['title','body']
    list_filter = ['status','created','publish','author']
    prepopulated_fields = {'slug':('title',)}
    # raw_id_fields = ['author',]
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created', 'approved']
    list_filter = ['approved', 'created']
    search_fields = ['author__username', 'body']
    actions  = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "approve selected comments"

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'location', 'experience_level',]
    list_filter = ['location','experience_level']
    search_fields = ['user__username', 'first_name', 'last_name', 'location', 'bio']
    fields = ['user', 'first_name', 'last_name', 'location', 'experience_level','favorite_gear','bio']
    




