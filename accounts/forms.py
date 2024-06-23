from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Profile


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['image',"username",'first_name','last_name','phone_number','email','gender','age','weight','height', "password1", "password2"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []