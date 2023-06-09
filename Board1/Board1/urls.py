"""
URL configuration for board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todolist import views
from todolist import cls_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', cls_views.CheckUser.as_view(), name="login"),
    path('', cls_views.PostList.as_view(), name="home"),
    path('discussed/', cls_views.DiscussedPost.as_view(), name='discussed'),
    path('users/', cls_views.ListUser.as_view(), name="users"),
    path('create_post/', cls_views.CreatePost.as_view(), name='create'),
    path('edit_error_post/', cls_views.CreatePost.as_view(), name='create_error'),
    path('post/', include("todolist.urls"))
]

