from django.shortcuts import render, redirect, reverse
from django.views import View
from user.forms import UserRegForm, UserLoginForm, ProfileEditForm
from user.models import User
from django.db import transaction
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class Profile(View):

    def get(self, request):
        return render(request, "registration/edit_user.html", {"form": ProfileEditForm()})

    def post(self, request):
        form = ProfileEditForm(request.POST)
        if not form.is_valid():
           return render(request, "registration/login.html", {"form": ProfileEditForm()})
        else:
           username_ = form_class.cleaned_data["username"]
           password_ = form_class.cleaned_data["password"]
           qs = User.objects.filter(username=username_)
           if not qs:
               return render(request, "registration/login.html", {"form_class": UserLoginForm()})
           else:
               if not qs.filter(password=password_):
                   return render(request, "registration/login.html", {"form_class": UserLoginForm()})
               else:
                   return redirect(reverse("home"))


class UserReg(View):

    def get(self, request):
        return render(request, "registration/registration.html", {"form": UserRegForm()})

    def post(self, request):
        form = UserRegForm(request.POST)
        if not form.is_valid():
            return render(request, "registration/registration.html", {"form": UserRegForm()})
        else:
            with transaction.atomic():
                username = form.cleaned_data["username"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                user = User(username=username, email=email, password=password)
                user.save()
                return redirect(reverse("login"))


class UserLogout(LogoutView):
    pass


class UserLogin(LoginView):
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url