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



    def image_tag(self, obj):
        return format_html('<img src="C:\Project\Board1\Board1\media\user.jpg" width="50" height="50" />'.format(obj.image.url))





