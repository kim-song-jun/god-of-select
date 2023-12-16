from django.urls import path

from . import views

urlpatterns = [
    path("", views.test, name="index"),

    path("test/create/<str:user_name>", views.test_create_user, name="test_create_user"),

    path("create/<str:user_name>", views.create_user, name="create_user"),

]