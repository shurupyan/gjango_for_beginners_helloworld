from django.urls import path
from .views import PostView, PostDetailView

urlpatterns = [
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", PostView.as_view(), name="home"),
]
