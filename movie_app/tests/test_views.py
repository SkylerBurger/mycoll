from django.test import TestCase
from django.urls import reverse

from movie_app.views import (
    MovieDetailView,
    MovieListView,
    MovieCopyDetailView,
    MovieCopyListView,
)


class MovieViewsTests(TestCase):
    def test_movie_list_view(self):
        response = self.client.get(reverse('movie_list'))
        # https://docs.djangoproject.com/en/3.1/topics/testing/tools/#django.test.Response.resolver_match
        self.assertEqual(response.resolver_match.func.__name__, MovieListView.as_view().__name__)
        self.assertEqual(response.status_code, 200)

    # TODO: complete test for 'movie_detail'
    # def test_movie_detail_view(self):
    #     movie = self.create_movie()
    #     url = reverse('movie_detail', args=[str(movie.id)])
    #     print(url)
    #     response = self.client.get(url)
    #     # Receiving a 404 back for some reason
    #     self.assertEqual(response.status_code, 200)


class MovieCopyViewsTests(TestCase):
    def test_moviecopy_list_view(self):
        response = self.client.get(reverse('movie_copy_list'))
        self.assertEqual(response.resolver_match.func.__name__, MovieCopyListView.as_view().__name__)
        self.assertEqual(response.status_code, 200)

    # TODO: test for 'movie_copy_detail'
    