from django.http import HttpRequest
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Event, User


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsListUser(BasePermission):

    def has_object_permission(self, request: HttpRequest, view, obj: User):
        if request.method in ["GET"] and request.user.is_staff:
            return True
        else:
            return False


class IsOwnerReadOnly(BasePermission):

    def has_object_permission(self, request: HttpRequest, view, obj: Event):
        if request.method in ["POST"]:
            return True
        else:
            return False

