from django.contrib.auth.models import AbstractUser
from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = dict(username=forms.TextInput(attrs={"class": "form-control"}),
                       password=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = dict(username=forms.TextInput(attrs={"class": "form-control"}),
                       email=forms.EmailInput(attrs={"class": "form-control"}),
                       password=forms.PasswordInput(attrs={"class": "form-control"}))


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email')


