from django.db import models

# Create your models here.


class ContactInquiry(models.Model):
    """
    This is a model for a user to
    make contact with the blog site.
    The user will supply details name,
    email and message.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inquiry from {self.name} - {self.email}'
