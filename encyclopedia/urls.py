from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.Random, name="random"),
    path("search", views.search, name="search"),
    path("wiki/<str:name>", views.display, name="display"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("create", views.create, name="create")
]
