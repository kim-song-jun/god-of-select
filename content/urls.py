from django.urls import path

from . import views

urlpatterns = [
    path("", views.test, name="index"),
    path("create", views.create_content, name="create_content"),
    path("search", views.search_content, name="search_content"),
]