from django.contrib.auth.models import AbstractUser
from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
                    "username": forms.TextInput(attrs={"class": "form-control"}),
                    "password": forms.PasswordInput(attrs={"class": "form-control"}),
                  }


class UserRegForm(UserCreationForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

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


