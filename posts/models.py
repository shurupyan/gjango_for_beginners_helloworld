from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, default="Post Title")
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        default=get_user_model().objects.get_by_natural_key(username="admin").pk,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
