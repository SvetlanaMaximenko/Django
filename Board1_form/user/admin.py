from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from user.models import User
from user.forms import ProfileEditForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from django.utils.html import format_html


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    # form = ProfileEditForm

    list_display = ('username', 'email', 'address', 'phone', 'avatar')

    @property
    def image_tag(self, obj):
        return format_html(f'<img src="" width="50" height="50" />')






