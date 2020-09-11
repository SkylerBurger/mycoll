from django.test import TestCase
from django.urls import reverse

from tv_app.views import (
    ShowDetailView,
    ShowListView,
    SeasonDetailView,
    SeasonListView,
    SeasonCopyDetailView,
    SeasonCopyListView,
)

class ShowViewsTests(TestCase):
    def test_show_list_view(self):
        response = self.client.get(reverse('show_list'))
        self.assertEqual(response.resolver_match.func.__name__, ShowListView.as_view().__name__)
        self.assertEqual(response.status_code, 200)

    # TODO: test for 'show_detail'


class SeasonViewsTests(TestCase):
    def test_season_list_view(self):
        response = self.client.get(reverse('season_list'))
        self.assertEqual(response.resolver_match.func.__name__, SeasonListView.as_view().__name__)
        self.assertEqual(response.status_code, 200)

    # TODO: test for 'season_detail'


class SeasonCopyViewsTests(TestCase):
    def test_season_copy_list_view(self):
        response = self.client.get(reverse('season_copy_list'))
        self.assertEqual(response.resolver_match.func.__name__, SeasonCopyListView.as_view().__name__)
        self.assertEqual(response.status_code, 200)

    # TODO: test for 'season_copy_detail'
