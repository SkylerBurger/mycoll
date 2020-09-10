from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import (
    Show,
    Season,
    SeasonCopy,
)


class ShowModelTests(TestCase):
    def setUp(self):
        # Dummy user
        self.user = get_user_model().objects.create_user(
            username='justatest',
            email='test@test.com',
            password='supersecret',
        )


class SeasonModelTests(TestCase):
    def setUp(self):
        pass