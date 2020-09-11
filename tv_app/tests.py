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
    def create_show(self):
        user = get_user_model().objects.create_user(
            username='justatest',
            email='test@test.com',
            password='supersecret',
        )
        show = Show.objects.create(
            owner=user,
            title='Sabrina the Teenage Witch',
            year_first_aired=1996,
            overview='Being a teen is difficult, being a teen witch is impossible.',
            image_link='www.google.com',
            tmdb_page_link='www.tmdb.org',
        )

        return show, user

    def test_show_absolute_url(self):
        show, user = self.create_show()
        expected = f'/api/v1/tv/{show.id}'
        actual = show._absolute_url
        self.assertEqual(expected, actual)

    def test_show_list_view(self):
        response = self.client.get(reverse('show_list'))
        self.assertEqual(response.resolver_match.func.__name__, ShowListView.as_view().__name__)
        self.assertEqual(response.status_code, 200)

    def test_show_content(self):
        show, user = self.create_show()
        self.assertEqual(show.owner.username, 'justatest')
        self.assertEqual(show.title, 'Sabrina the Teenage Witch')
        self.assertEqual(show.year_first_aired, 1996)
        self.assertEqual(show.overview, 'Being a teen is difficult, being a teen witch is impossible.')
        self.assertEqual(show.image_link, 'www.google.com')
        self.assertEqual(show.tmdb_page_link, 'www.tmdb.org')

    def test_show_str(self):
        show, user = self.create_show()
        expected = 'Sabrina the Teenage Witch (1996)'
        actual = str(show)
        self.assertEqual(actual, expected)

class SeasonModelTests(TestCase):
    def setUp(self):
        pass

    def create_season(self):
        user = get_user_model().objects.create_user(
            username='justatest',
            email='test@test.com',
            password='supersecret',
        )
        show = Show.objects.create(
            owner=user,
            title='Sabrina the Teenage Witch',
            year_first_aired=1996,
            overview='Being a teen is difficult, being a teen witch is impossible.',
            image_link='www.google.com',
            tmdb_page_link='www.tmdb.org',
        )
        season = Season.objects.create(
            owner=user,
            show=show,
            season_number=1,
            episode_count=23,
            year_first_aired=1996,
            overview='Things are just getting started!',
            image_link='www.google.com',
            tmdb_page_link='www.tmdb.org',
        )

        return season

    def test_season_absolute_url(self):
        season = self.create_season()
        expected = '/api/v1/tv/season/1'
        actual = season._absolute_url
        self.assertEqual(actual, expected)


class SeasonCopyModelTests(TestCase):
    def setUp(self):
        pass