from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)


