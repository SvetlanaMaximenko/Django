import datetime
from turtle import title

# from generic import DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db import models
from django.http import Http404
from django.urls import reverse_lazy
from .models import Post


class PostList(View):

    @staticmethod
    def get_queryset():
        return Post.objects.all()

    def get(self, request):
        posts = self.get_queryset()
        return render(request, "todolist/home.html", {"posts": posts})


class CreatePost(View):

    def get(self, request):
        return render(request, "todolist/create_post.html")

    @staticmethod
    def is_valid_title(title: str) -> bool:
        return bool(title)

    @staticmethod
    def is_valid_content(content: str) -> bool:
        return bool(content)

    def save_post(self):
        return self.save()

    def post(self, request):
        title = request.POST.get("title")
        content = request.POST.get("content")
        # errors = []
        # if not self.is_valid_title(title) or not self.is_valid_content(content):
        #     # errors.append("Укажите заголовок и содержимое")
        #     return redirect(request, "edit_error_post.html")
        # else:
        post = Post(title=title, content=content)
        post.save()
        return redirect("/")

            # render(request, "todolist/create_post.html", {"errors": errors})


class ShowPost(View):

   def get(self, request, post_id: int):
        post = Post.objects.get(id=post_id)
        return render(request, "todolist/show_post.html", {"post": post})


class DeletePost(View):

    def get(self, request, post_id: int):
        post = Post.objects.get(id=post_id)
        return render(request, "todolist/delete_post.html", {"post": post})

    def post(self, request, post_id: int):

        post = Post.objects.get(id=post_id)
        post.delete()
        posts = PostList.get_queryset()
        return render(request, "todolist/home.html", {"posts": posts})


class EditPost(View):

    @staticmethod
    def is_valid_title(title: str) -> bool:
        return bool(title)

    @staticmethod
    def is_valid_content(content: str) -> bool:
        return bool(content)

    def get(self, request, post_id: int):
        post = Post.objects.get(id=post_id)
        return render(request, "todolist/edit_post.html", {"post": post})

    def post(self, request, post_id: int):
        title = request.POST.get("title")
        content = request.POST.get("content")
        post = Post.objects.get(id=post_id)
        post.delete()
        # errors = []
        # if not self.is_valid_title(title) or not self.is_valid_content(content):
        #     errors.append("Укажите заголовок и содержимое")
        #     return render(request, "todolist/edit_error_post.html")
        # else:
        post = Post(title=title, content=content)
        post.save()
        return redirect("/")











