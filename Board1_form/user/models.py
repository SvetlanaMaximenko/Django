from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=250, null=True)
    avatar = models.ImageField("Аватар пользователя", upload_to="C:/Project/Board1/Board1/media/",
                               default="C:/Project/Board1/Board1/media/unAuth.jpg", blank=True, null=True)

    class Meta:
        db_table = "user"


