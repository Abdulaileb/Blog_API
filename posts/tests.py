from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

class BlogTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test",
            email="test@example.com",
            password="secret",
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="A good user",
            body="Nice body",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "test")
        self.assertEqual(self.post.title, "A good user")
        self.assertEqual(self.post.body, "Nice body")
        self.assertEqual(str(self.post), "A good user")
