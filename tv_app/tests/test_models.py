from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tv_app.models import (
    Show,
    Season,
    SeasonCopy,
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

        return show

    def test_show_absolute_url(self):
        show = self.create_show()
        expected = f'/api/v1/tv/{show.id}'
        actual = show._absolute_url
        self.assertEqual(expected, actual)

    def test_show_content(self):
        show = self.create_show()
        self.assertEqual(show.owner.username, 'justatest')
        self.assertEqual(show.title, 'Sabrina the Teenage Witch')
        self.assertEqual(show.year_first_aired, 1996)
        self.assertEqual(show.overview, 'Being a teen is difficult, being a teen witch is impossible.')
        self.assertEqual(show.image_link, 'www.google.com')
        self.assertEqual(show.tmdb_page_link, 'www.tmdb.org')

    def test_show_str(self):
        show = self.create_show()
        expected = 'Sabrina the Teenage Witch (1996)'
        actual = str(show)
        self.assertEqual(actual, expected)


class SeasonModelTests(TestCase):
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
            title='Season One',
            overview='Things are just getting started!',
            image_link='www.google.com',
            tmdb_page_link='www.tmdb.org',
        )

        return season

    def test_season_absolute_url(self):
        season = self.create_season()
        expected = f'/api/v1/tv/season/{season.id}'
        actual = season._absolute_url
        self.assertEqual(actual, expected)

    def test_season_content(self):
        season = self.create_season()
        self.assertEqual(season.owner.username, 'justatest')
        self.assertEqual(season.show.title, 'Sabrina the Teenage Witch')
        self.assertEqual(season.title, 'Season One')
        self.assertEqual(season.season_number, 1)
        self.assertEqual(season.episode_count, 23)
        self.assertEqual(season.year_first_aired, 1996)
        self.assertEqual(season.overview, 'Things are just getting started!')
        self.assertEqual(season.image_link, 'www.google.com')
        self.assertEqual(season.tmdb_page_link, 'www.tmdb.org')

    def test_season_str(self):
        season = self.create_season()
        expected = 'Sabrina the Teenage Witch - Season 1'
        actual = str(season)
        self.assertEqual(actual, expected)


class SeasonCopyModelTests(TestCase):
    def create_season_copy(self):
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
            title='Season One',
            overview='Things are just getting started!',
            image_link='www.google.com',
            tmdb_page_link='www.tmdb.org',
        )
        season_copy = SeasonCopy.objects.create(
            owner=user,
            season=season,
            platform='Amazon Prime Video',
            form='VOD',
            vod_link='www.amazon.com',
        )

        return season_copy

    def test_season_copy_absolute_url(self):
        season_copy = self.create_season_copy()
        expected = f'/api/v1/tv/season/copy/{season_copy.id}'
        actual = season_copy._absolute_url
        self.assertEqual(actual, expected)

    def test_season_copy_content(self):
        season_copy = self.create_season_copy()
        self.assertEqual(season_copy.owner.username, 'justatest')
        self.assertEqual(str(season_copy.season), 'Sabrina the Teenage Witch - Season 1')
        self.assertEqual(season_copy.platform, 'Amazon Prime Video')
        self.assertEqual(season_copy.form, 'VOD')
        self.assertEqual(season_copy.vod_link, 'www.amazon.com')

    def test_season_copy_str(self):
        season = self.create_season_copy()
        expected = 'justatest\'s VOD of Sabrina the Teenage Witch season 1 on Amazon Prime Video'
