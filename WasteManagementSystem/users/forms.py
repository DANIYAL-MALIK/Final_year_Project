from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models


class UserCreateForm(UserCreationForm):
    isManager = models.BooleanField(default=False)
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('isManager',)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']