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
    def create_movie(self):
        user = get_user_model().objects.create_user(
            username='justatest',
            email='test@test.com',
            password='supersecret',
        )
        movie = Movie.objects.create(
            owner=user,
            title='Sphere',
            release_year=1998,
            overview='Something is at the bottom of the ocean!',
            mpaa_rating='R',
            runtime_minutes=120,
            image_link='www.google.com',
            tmdb_page_link='www.google.com',
        )

        return movie

    def test_movie_content(self):
        movie = self.create_movie()
        self.assertEqual(movie.owner.username, 'justatest')
        self.assertEqual(movie.title, 'Sphere')
        self.assertEqual(movie.release_year, 1998)
        self.assertEqual(movie.overview, 'Something is at the bottom of the ocean!')
        self.assertEqual(movie.mpaa_rating, 'R')
        self.assertEqual(movie.runtime_minutes, 120)
        self.assertEqual(movie.image_link, 'www.google.com')
        self.assertEqual(movie.tmdb_page_link, 'www.google.com')

    def test_movie_str(self):
        movie = self.create_movie()
        expected = 'Sphere (1998)'
        actual = str(movie)
        self.assertEqual(actual, expected)

    def test_movie_absolute_url(self):
        movie = self.create_movie()
        expected = f'/api/v1/movies/{movie.id}'
        actual = movie._absolute_url
        self.assertURLEqual(actual, expected)

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
    def create_movie_copy(self):
        user = get_user_model().objects.create_user(
            username='justatest',
            email='test@test.com',
            password='supersecret',
        )
        movie = Movie.objects.create(
            owner=user,
            title='Sphere',
            release_year=1998,
            overview='Something is at the bottom of the ocean!',
            mpaa_rating='R',
            runtime_minutes=120,
            image_link='www.google.com',
            tmdb_page_link='www.google.com',
        )
        movie_copy = MovieCopy.objects.create(
            movie=movie,
            owner=user,
            platform='Amazon Prime Video',
            form='VOD',
            vod_link='amazon.com',
        )

        return movie_copy

    def test_movie_copy_absolute_url(self):
        movie_copy = self.create_movie_copy()
        expected = f'/api/v1/movies/copies/{movie_copy.id}'
        actual = movie_copy._absolute_url
        self.assertURLEqual(actual, expected)

    def test_moviecopy_content(self):
        movie_copy = self.create_movie_copy()
        self.assertEqual(movie_copy.owner.username, 'justatest')
        self.assertEqual(movie_copy.movie.title, 'Sphere')
        self.assertEqual(movie_copy.platform, 'Amazon Prime Video')
        self.assertEqual(movie_copy.form, 'VOD')
        self.assertEqual(movie_copy.vod_link, 'amazon.com')

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
        movie_copy = self.create_movie_copy()
        expected = 'justatest\'s VOD of Sphere on Amazon Prime Video'
        actual = str(movie_copy)
        self.assertEqual(actual, expected)
    