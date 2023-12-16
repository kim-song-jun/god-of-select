from django.urls import path

from . import views

urlpatterns = [
    path("", views.test, name="index"),
    path("test/create/<uuid:user_id>", views.test_create, name="test_create"),
    path("test/search/<uuid:user_id>", views.test_search, name="test_search"),
    path("test/vote/<uuid:user_id>", views.test_vote, name="test_vote"),
    path("create", views.create_issue, name="create_issue"),
    path("search", views.search_issue, name="search_issue"),
    path("search/hot", views.search_hot_issue, name="search_hot_issue"),
    path("search/all", views.search_all_issue, name="search_all_issue"),
    path("vote", views.vote_issue, name="vote_issue"),
]