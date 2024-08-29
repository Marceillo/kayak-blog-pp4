from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_kayaking, name='about_kayaking'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
