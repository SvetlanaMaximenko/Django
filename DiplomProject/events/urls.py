from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('<int:event_id>/view/', views.EventView.as_view(), name="view"),
    path('<int:event_id>/edit/', views.EventEdit.as_view(), name="edit"),
    path('<int:event_id>/comment/add/', views.AddComment.as_view(), name="add"),
]