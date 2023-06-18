from audioop import reverse
from turtle import title

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
# Create your views here.




def home(request):
    print(request.user)
    posts = Post.objects.all()
    return render(request, "todolist/home.html", {"posts": posts})


def create_post(request):
    errors = []
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("text")
        errors = []
        if not title or not content:
            errors.append("Укажите заголовок и содержимое")
        else:
            post = Post(title=title, content=content)
            post.save()
            return redirect("/")

    return render(request, "todolist/create_post.html", {"errors": errors})


def show_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "todolist/show_post.html", {"post": post})


def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    # post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("/")


def show_edit_form(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "todolist/edit_post.html", {"post": post})


def edit_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    title = request.POST.get("title")
    content = request.POST.get("text")

    if title == "" or content == "":
        post = Post(title=title, content=content)
        return render(request, "todolist/edit_error_post.html", {"post": post})

    else:
        post = Post(title=title, content=content)
        post.save()
        return redirect("/")
        #return render(request, "show_post.html", {"post": post})
