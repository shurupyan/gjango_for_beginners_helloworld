from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post


# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword", email="testemail@example.com"
        )
        cls.post = Post.objects.create(
            title="This is a good test title!",
            body="This is a good test body",
            author=cls.user,
        )

    def test_model_content(self):
        self.assertEqual(self.post.title, "This is a good test title!")
        self.assertEqual(self.post.body, "This is a good test body")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "This is a good test title!")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a good test title!")
        self.assertContains(response, "This is a good test body")

    def test_post_detailpage(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_detail.html")
        self.assertContains(response, "This is a good test title!")
        self.assertContains(response, "This is a good test body")

    def test_inexistent_post_detailpage(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": 10000}))
        self.assertEqual(response.status_code, 404)

    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"),
            {"title": "New title", "body": "New body", "author": self.user.pk},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New body")

    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {"title": "Updated title", "body": "Updated body", "author": self.user.pk},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated body")

    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
