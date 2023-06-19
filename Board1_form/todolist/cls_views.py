from datetime import datetime, timedelta
# from generic import DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.http import Http404

from user.forms import UserRegForm, UserLoginForm
from user.models import User
from django.db.models import Count, Max
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models.query import Q, QuerySet
from todolist.forms import PostForm
from django.db import transaction
from todolist.models import Post, Tag, Comment


class PostList(View):

    def get_queryset(self):
        search = self.request.GET.get("search_str")
        if search:
            qs = Post.objects.all().select_related("user").annotate(comment_count=Count('comments'))\
                .values("id", "title", "created", "user").filter(Q(title__icontains=search))
        else:
            qs = Post.objects.all().select_related("user").annotate(comment_count=Count('comments')) \
                .values("id", "title", "created", "user")

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


class UserLogin(View):

    def get(self, request):
        return render(request, "registration/login.html", {"form": UserLoginForm()})

    def post(self, request):
        form = UserLoginForm(request.POST)

        if not form.is_valid():
            print(form)
            return render(request, "registration/login.html", {"form": UserLoginForm()})
        else:
            username_ = form.cleaned_data["username"]
            password_ = form.cleaned_data["password"]
            qs = User.objects.filter(username=username_)

            if not qs:
                return render(request, "registration/login.html", {"form": UserLoginForm()})
            else:
                if not qs.filter(password=password_):
                    return render(request, "registration/login.html", {"form": UserLoginForm()})
                else:
                    return redirect(reverse("home"))


class UserReg(View):

    @staticmethod
    def get_queryset():
        return User.objects.all()

    def get(self, request):
        return render(request, "registration/registration.html", {"form": UserRegForm()})

    def post(self, request):
        form = UserRegForm(request.POST)
        if not form.is_valid():
            return render(request, "registration/registration.html", {"form": UserRegForm()})
        else:
            with transaction.atomic():
                username = form.cleaned_data["username"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                user = User(username=username, email=email, password=password)
                user.save()
                return redirect(reverse("home"))


@method_decorator(login_required, name='dispatch')
class CreatePost(View):

    def get(self, request):
        tags = Tag.objects.values_list("name", flat=True)
        # print(tags_list)
        return render(request, "todolist/create_post.html", {"form": PostForm()})

    def post(self, request):
        form = PostForm(request.POST)
        if not form.is_valid():
            return render(request, "todolist/create_post.html", {"form": PostForm()})
        else:
            with transaction.atomic():
                title = form.cleaned_data["title"]
                content = form.cleaned_data["content"]
                tags: QuerySet[Tag] = form.cleaned_data["tags"]
                post = Post(title=title, content=content, user_id=request.user.id)

                post.save()
                post.tags.add(*list(tags))
            return redirect(reverse("home"))


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











