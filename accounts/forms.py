from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    usable_password = None
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")