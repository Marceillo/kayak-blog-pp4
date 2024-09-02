from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_kayaking, name='about_kayaking'),
    path('contact_kayaker/', views.contact_kayaker, name='contact_kayaker'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
