from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('user_profile/', views.userprofile, name='user_profile'),
    path('profile_edit/',views.profile_edit, name='profile_edit')
]