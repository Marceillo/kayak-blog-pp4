from django.urls import path
from . import views

 


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('user_profile/', views.userprofile, name='user_profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('delete_profile_picture', views.delete_profile_picture, name='delete_profile_picture'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('post/new', views.Create_Kayak_Post_View.as_view(), name='create_kayak_post'),
    path('post/<slug:slug>/edit/', views.Update_Kayak_Post_View.as_view(), name='update_kayak_post'),
    path('post/<slug:slug>/delete/', views.Delete_Kayak_Post_View.as_view(), name='delete_kayak_post'),
    path('my-posts/', views.My_Post_List_View.as_view(), name='my_post_list'),
    path('search/', views.kayak_search_result, name='kayak_search_result'),
    
    

]