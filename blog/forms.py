from django import forms 
from .models import UserProfile, Post 


class UserProfileForm( forms.ModelForm ):
    email = forms.EmailField(
        required=False, widget=forms.EmailInput(attrs={'id': 'user-email', 'name': 'user-email', 'autocomplete': 'email'})
    )
    class Meta:
        model = UserProfile 
        fields = [ 'profile_picture','first_name', 'last_name','email', 'location', 'experience_level', 'favorite_gear', 'bio']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['title', 'body', 'status', 'excerpt', 'blog_image']
        widgets = {
        'body': forms.Textarea(attrs={'rows': 10}),
        'excerpt': forms.Textarea(attrs={'rows': 3}),
    }

    # Excerpt to generate automatically
    def save (self, commit=True ):
        instance = super().save(commit=False)
        if not instance.excerpt:
            instance.excerpt = instance.body[:197] + '...' if len(instance.body) > 197 else instance.body
        if commit:
            instance.save()
            return instance


class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=100, required=False)

    #def __init__(self, *args, **kwargs):
    #    super(PostForm, self).__init__(*args, **kwargs)
    #    if self.instance and self.instance.pk:
    #        self.fields['delete_image'].widget.attrs.update({'class': 'form-check-input'})


       