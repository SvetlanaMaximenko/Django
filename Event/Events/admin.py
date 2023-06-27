from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import User, Event


@register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "meeting_time", "description"]

    @admin.display(description="Подписчики", boolean=True)
    def users_list(self, obj: Event):
        return list(obj.users.values_list("username", flat=True))


@register(User)
class UserAdmin(admin.ModelAdmin):
    pass

