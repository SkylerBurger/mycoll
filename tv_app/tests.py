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
        self.show = Show.objects.create(
            owner=self.user,
            title='Sabrina the Teenage Witch',
            year_first_aired=1996,
            overview='Being a teen is difficult, being a teen witch is impossible.',
            image_link='www.google.com',
            tmdb_page_link='www.tmdb.org',
        )

    def test_show_absolute_url(self):
        expected = '/api/v1/tv/1'
        actual = self.show._absolute_url
        self.assertEqual(expected, actual)

    def test_show_list_view(self):
        response = self.client.get(reverse('show_list'))
        self.assertEqual(response.status_code, 200)


class SeasonModelTests(TestCase):
    def setUp(self):
        pass


class SeasonCopyModelTests(TestCase):
    def setUp(self):
        pass