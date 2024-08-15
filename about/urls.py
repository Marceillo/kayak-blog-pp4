from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_kayaking, name='about_kayaking'),
    path('contact/', about_views.contact_us, name='contact'),
]