from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class LoginForm(UserCreationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
