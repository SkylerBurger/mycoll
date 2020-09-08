from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import (
    Movie,
    MovieCopy,
)


class MovieAppTests(TestCase):
    def setUp(self):
        # Dummy user
        self.user = get_user_model().objects.create_user(
            username='justatest',
            email='test@test.com',
            password='supersecret',
        )
        # Dummy Movie
        self.movie = Movie.objects.create(
            owner=self.user,
            title='Sphere',
            release_year=1998,
            overview='Something is at the bottom of the ocean!',
            mpaa_rating='R',
            runtime_minutes=120,
            image_link='www.google.com',
            tmdb_page_link='www.google.com',
        )
        # Dummy MovieCopy
        self.movie_copy = MovieCopy.objects.create(
            movie=self.movie,
            owner=self.user,
            platform='Amazon Prime Video',
            form='VOD',
            vod_link='amazon.com',
        )

    # Movie Model Tests
    def test_movie_content(self):
        self.assertEqual(self.movie.owner.username, 'justatest')
        self.assertEqual(self.movie.title, 'Sphere')
        self.assertEqual(self.movie.release_year, 1998)
        self.assertEqual(self.movie.overview, 'Something is at the bottom of the ocean!')
        self.assertEqual(self.movie.mpaa_rating, 'R')
        self.assertEqual(self.movie.runtime_minutes, 120)
        self.assertEqual(self.movie.image_link, 'www.google.com')
        self.assertEqual(self.movie.tmdb_page_link, 'www.google.com')

    def test_movie_str(self):
        expected = 'Sphere (1998)'
        actual = str(self.movie)
        self.assertEqual(actual, expected)

    def test_movie_absolute_url(self):
        self.assertEqual(self.movie._absolute_url, '/api/v1/movies/1')

    # MovieCopy Model Tests
    def test_moviecopy_str(self):
        expected = 'justatest\'s VOD of Sphere on Amazon Prime Video'
        actual = str(self.movie_copy)
        self.assertEqual(actual, expected)