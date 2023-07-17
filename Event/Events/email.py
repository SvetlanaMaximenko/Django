from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import AbstractUser
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string


class BaseEmailSender:
    user_field = "id"


class EmailSender(BaseEmailSender):

    def get_context(self) -> dict:
        ctx = super().get_context()
        ctx["variable"] = "Привет"
        return ctx


