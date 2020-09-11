from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import (
    Show,
    Season,
    SeasonCopy,
)
from .views import (
    ShowDetailView,
    ShowListView,
    SeasonDetailView,
    SeasonListView,
    SeasonCopyDetailView,
    SeasonCopyListView,
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
        self.assertEqual(response.resolver_match.func.__name__, ShowListView.as_view().__name__)
        self.assertEqual(response.status_code, 200)

    def test_show_content(self):
        self.assertEqual(self.show.owner.username, 'justatest')
        self.assertEqual(self.show.title, 'Sabrina the Teenage Witch')
        self.assertEqual(self.show.year_first_aired, 1996)
        self.assertEqual(self.show.overview, 'Being a teen is difficult, being a teen witch is impossible.')
        self.assertEqual(self.show.image_link, 'www.google.com')
        self.assertEqual(self.show.tmdb_page_link, 'www.tmdb.org')

    def test_show_str(self):
        expected = 'Sabrina the Teenage Witch (1996)'
        actual = str(self.show)
        self.assertEqual(actual, expected)

class SeasonModelTests(TestCase):
    def setUp(self):
        pass


class SeasonCopyModelTests(TestCase):
    def setUp(self):
        pass