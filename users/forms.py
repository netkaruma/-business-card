# users/forms.py

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField() 
    password2 = forms.CharField() 
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1','password2']

class CustomUserAuthForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']