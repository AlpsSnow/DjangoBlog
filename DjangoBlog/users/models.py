from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

# Create your models here.
class UserRegisterForm(UserCreationForm):
    class Mata:
        model = User
        fields = ['username','password1','password2']