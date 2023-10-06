from django.shortcuts import render, redirect, reverse
from django.views import View
from user.forms import UserRegForm, UserLoginForm, ProfileEditForm
from user.models import User
from events.models import Event
from django.db import transaction
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        # Ваш код здесь
        return context


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
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            events = Event.objects.all()
            return render(request, "events/home.html", {"events": events})
        else:
            # messages.error(request, 'Ошибка валидации формы')
            return render(request, "registration/registration.html", {"form": UserRegForm()})


class UserLogout(LogoutView):
    success_url = reverse_lazy('home')


class UserLogin(LoginView):
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

    # def post(self, request):
    #     form = UserLoginForm(data=request.POST)
    #     print('22222')
    #     if form.is_valid():
    #         print('1111111111111')
    #         user = form.get_user()
    #         login(request, user)
    #         messages.success(request, 'You have successfully logged in.')
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'Invalid username or password.')
        # if not form.is_valid():
        #     return render(request, "login")
        # else:
        #     username = form.cleaned_data.get('username')
        #     password = form.cleaned_data.get('password')
        #     user = User(username=username, password=password)
        #     users = User.objects.all()
        #     if user in users:
        #         return redirect('home')
