from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="posts")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


