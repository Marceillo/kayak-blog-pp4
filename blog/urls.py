from django.urls import path
from . import views
from .views import BlogPasswordChangeView 


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('user_profile/', views.userprofile, name='user_profile'),
    path('profile_edit/',views.profile_edit, name='profile_edit'),
    path('delete_profile/',views.delete_profile, name='delete_profile'),
    path('accounts/password/change/', BlogPasswordChangeView.as_view(),name='account_password_change')
]