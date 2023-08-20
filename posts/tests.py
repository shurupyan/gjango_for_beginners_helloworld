from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "<h1>Message board homepage</h1>")
        self.assertContains(response, "This is a test!")
