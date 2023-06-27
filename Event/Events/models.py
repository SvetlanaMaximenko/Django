from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers


class User(AbstractUser):

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username


class Event(models.Model):
    name = models.CharField(max_length=200)
    meeting_time = models.DateTimeField()
    description = models.CharField(max_length=500)
    users = models.ManyToManyField(User, related_name="events")

    def __str__(self):
        return self.name



