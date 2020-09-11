from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import (
    Movie,
    MovieCopy,
)
from .views import (
    MovieDetailView,
    MovieListView,
    MovieCopyDetailView,
    MovieCopyListView,
)

import json

class MovieModelTests(TestCase):
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
        self.assertURLEqual(self.movie._absolute_url, '/api/v1/movies/5')

    def test_movie_list_view(self):
        response = self.client.get(reverse('movie_list'))
        # https://docs.djangoproject.com/en/3.1/topics/testing/tools/#django.test.Response.resolver_match
        self.assertEqual(response.resolver_match.func.__name__, MovieListView.as_view().__name__)
        self.assertEqual(response.status_code, 200)
        # Need to dig deeper into 'response' to find JSON content

    # def test_movie_detail_view(self):
    #     movie = Movie.objects.all()[0]
    #     url = reverse('movie_detail', args=[str(movie.id)])
    #     print(url)
    #     response = self.client.get(url)
    #     # Receiving a 404 back for some reason
    #     self.assertEqual(response.status_code, 200)


class MovieCopyModelTests(TestCase):
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

    def test_moviecopy_absolute_url(self):
        # ID is 5 because this is the 6th test function that has run setUp()
        # Tests seems to be run in alphabetical order by method name
        self.assertURLEqual(self.movie_copy._absolute_url, '/api/v1/movies/copies/1')

    def test_moviecopy_content(self):
        self.assertEqual(self.movie_copy.owner.username, 'justatest')
        self.assertEqual(self.movie_copy.movie.title, 'Sphere')
        self.assertEqual(self.movie_copy.platform, 'Amazon Prime Video')
        self.assertEqual(self.movie_copy.form, 'VOD')
        self.assertEqual(self.movie_copy.vod_link, 'amazon.com')

    def test_moviecopy_list_view(self):
        response = self.client.get(reverse('movie_copy_list'))
        self.assertEqual(response.resolver_match.func.__name__, MovieCopyListView.as_view().__name__)
        self.assertEqual(response.status_code, 200)

    # def test_moviecopy_detail_view(self):
    #     copy = MovieCopy.objects.all()[0]
    #     url = reverse('movie_copy_detail', args=[str(copy.id)])
    #     print(url)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    
    def test_moviecopy_str(self):
        expected = 'justatest\'s VOD of Sphere on Amazon Prime Video'
        actual = str(self.movie_copy)
        self.assertEqual(actual, expected)
    