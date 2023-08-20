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
