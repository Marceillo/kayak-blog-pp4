from . import views 
from django.urls import path 

urlpatterns = [
    path('', views.about_kayaking, name='about_kayaking'),
]