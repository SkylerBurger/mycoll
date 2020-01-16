from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Book


class BookTestCase(TestCase):
    def setUp(self):
        # Create dummy user
        self.user = get_user_model().objects.create_user(
            'username': 'test_user',
            'email': 'email@email.com',
            'password': 'secret',
        )
        # Create dummy book
        self.book = Book.objects.create(
            'title': 'Sphere',
            'author': 'Michael Crichton',
            'published': 1990,
            'owner': self.user
        )

    def test_stored_book(self):
        # These tests require Views to generate responses
        pass
