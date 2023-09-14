from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from user.models import User
from django.utils.html import format_html


@admin.register(User)
class UserAdmin(DefaultUserAdmin):

    list_display = ('username', 'email')

    # def image_tag(self, obj):
    #     return format_html(f'<img src={ obj.avatar.url } width="50" height="50" />')
    #
    # image_tag.shot_description = 'Thumb'
    # image_tag.allow_tags = True
