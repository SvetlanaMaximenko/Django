from datetime import datetime, timedelta
# from generic import DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db import models
from django.http import Http404
from django.urls import reverse_lazy
from .models import Post, Tag
from user.models import User
from django.db.models import Count, Max
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PostList(View):

    @staticmethod
    def get_queryset():
        qs = Post.objects.annotate(comment_count=Count('comments'))
        return qs

    def get(self, request):
        posts = self.get_queryset()
        return render(request, "todolist/home.html", {"posts": posts})


class ListUser(View):

    @staticmethod
    def get_queryset():
        qs = User.objects.annotate(posts_count=Count('posts')).annotate(last_post=Max('posts__created')).order_by('-posts_count', '-last_post')

        return qs

    def get(self, request):
        users = self.get_queryset()
        return render(request, "todolist/list_user.html", {"users": users})


class DiscussedPost(View):
    @staticmethod
    def get_queryset():
        qs = Post.objects.filter(comments__created__gte=(datetime.now() - timedelta(hours=12))).annotate(num_comments=Count('comments')).order_by('-num_comments')
        return qs

    def get(self, request):
        posts = self.get_queryset()
        return render(request, "todolist/list_comments.html", {"posts": posts})


class CheckUser(View):

    @staticmethod
    def get_queryset():
        return User.objects.all()

    def get(self, request):
        return render(request, "registration/login.html")

    def is_valid_login(self, username: str, password: str) -> bool:
        return User.objects.filter(username=username, password=password)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        err = []
        if not self.is_valid_login(username, password):
            err.append("Неверный логин или пароль")
            return redirect(request, "todolist/edit_error_post.html")
        else:
            posts = PostList.get_queryset()
            return render(request, "todolist/home.html", {"posts": posts})
            # post = Post(title=title, content=content)
            # post.save()
            # posts = PostList.get_queryset()
            # return render(request, "todolist/home.html", {"posts": posts})


@method_decorator(login_required, name='dispatch')
class CreatePost(View):

    def get(self, request):
        tags_list = Tag.objects.values_list("name", flat=True)
        print(tags_list)
        return render(request, "todolist/create_post.html", {"tags_list": tags_list})

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

        errors = []
        if not self.is_valid_title(title) or not self.is_valid_content(content):
            errors.append("Укажите заголовок и содержимое")
            return redirect(request, "edit_error_post.html")
        else:
            post = Post(title=title, content=content, user_id=1)
            post.save()
            posts = PostList.get_queryset()
            return redirect("/")


class ShowPost(View):

   def get(self, request, post_id: int):
        post = Post.objects.get(id=post_id)
        return render(request, "todolist/show_post.html", {"post": post})


@method_decorator(login_required, name='dispatch')
class DeletePost(View):

    def get(self, request, post_id: int):
        post = Post.objects.get(id=post_id)
        return render(request, "todolist/delete_post.html", {"post": post})

    def has_object_permission(self, post: Post) -> bool:
        return post.user.id == self.request.user.id

    def post(self, request, post_id: int):

        post = Post.objects.get(id=post_id)
        if self.has_object_permission(post):
            post.delete()
            posts = PostList.get_queryset()
            return render(request, "todolist/home.html", {"posts": posts})
        else:
            return redirect(request, "edit_error_post.html")


@method_decorator(login_required, name='dispatch')
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

        errors = []
        if not self.is_valid_title(title) or not self.is_valid_content(content):
            errors.append("Укажите заголовок и содержимое")
            return render(request, "todolist/edit_error_post.html")
        else:
            post.title = title
            post.content = content
            post.user_id = post.user.id
            post.save()
            posts = Post.objects.all()
            return render(request, "todolist/home.html", {"posts": posts})











