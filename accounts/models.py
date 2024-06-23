from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    image = models.ImageField(upload_to='profile',blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique=True)
    age = models.PositiveIntegerField(default=20)
    height = models.PositiveIntegerField(default=170)
    weight = models.PositiveIntegerField(default=70)
    gender = models.CharField(max_length=6,default="Male",choices=GENDER_CHOICES)
    def __str__(self):
        return self.username
    
class Profile(models.Model):

    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username}'s Profile"