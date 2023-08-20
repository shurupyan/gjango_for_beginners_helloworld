from django.urls import path
from .views import (
    PostView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/new", PostCreateView.as_view(), name="post_new"),
    path("", PostView.as_view(), name="home"),
]
