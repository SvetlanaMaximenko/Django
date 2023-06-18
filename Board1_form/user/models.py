from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=250, null=True)
    avatar = models.ImageField("Аватар пользователя", upload_to="avatars/",
                               default="default/unAuth.jpg")
    
    class Meta:
        db_table = "user"
