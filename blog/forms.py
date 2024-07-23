from django import forms 
from .models import UserProfile 


class UserProfileForm( forms.ModelForm ):
    class Meta:
        model = UserProfile 
        fields = [ 'profile_picture','first_name', 'last_name', 'location', 'experience_level', 'favorite_gear', 'bio']
       