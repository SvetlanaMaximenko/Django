from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass

# class MyUserCreationForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = ("username", "phone", "address")
#
#
# class MyUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = User
#         fields = ("username", "phone", "address")
#
#
# class MyUserAdmin(UserAdmin):
#     form = MyUserChangeForm
#     add_form = MyUserCreationForm
#
#
# admin.site.unregister(User)
# admin.site.register(User, MyUserAdmin)


