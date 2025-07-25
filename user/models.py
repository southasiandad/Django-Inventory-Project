from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    image = models.ImageField(default='default avatar.jpg', upload_to='profile_images')
    
    def __str__(self):
        return f'{self.customer.username}-Profile'