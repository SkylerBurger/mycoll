import json

from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse, JsonResponse

import requests
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    Movie, 
    MovieCopy,
)
from .serializers import (
    MovieSerializer,
    MovieCopySerializer,
)


class MyMoviesMixin:
    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user = self.request.user
            return Movie.objects.all().filter(owner=user)
        else:
            return None


class MyMovieCopiesMixin:
    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user = self.request.user
            return MovieCopy.objects.all().filter(owner=user)
        else:
            return None


class MovieDetailView(MyMoviesMixin, RetrieveUpdateDestroyAPIView):
    model = Movie
    serializer_class = MovieSerializer


class MovieListView(MyMoviesMixin, ListCreateAPIView):
    model = Movie
    serializer_class = MovieSerializer


class MovieCopyDetailView(MyMovieCopiesMixin, RetrieveUpdateDestroyAPIView):
    model = MovieCopy
    serializer_class = MovieCopySerializer


class MovieCopyListView(MyMovieCopiesMixin, ListCreateAPIView):
    model = MovieCopy
    serializer_class = MovieCopySerializer


def generate_tmdb_search_url(query):
    """Generates the URL needed to request movie search results from TMDb."""
    base_url = 'https://api.themoviedb.org/3/search/movie'
    api_key = '?api_key=' + '067c757c5122bd33acc966e32828544c'
    query_param = '&query=' + query

    return base_url + api_key + query_param


def generate_tmdb_details_url(movie_id):
    """Generates the URL needed to request movie details from TMDb."""
    base_url = 'https://api.themoviedb.org/3/movie/'
    api_key = '?api_key=' + '067c757c5122bd33acc966e32828544c'
    append_release_dates = '&append_to_response=release_dates'

    return base_url + movie_id + api_key + append_release_dates


def generate_tmdb_poster_path(path):
    """Generates URL for movie poster image with results from TMDb."""
    poster_path_url = ''
    base_url = 'https://image.tmdb.org/t/p/w500'
    
    if path != None:
        poster_path_url = base_url + path
    
    return poster_path_url


def truncate_tmdb_release_date(release_date):
    """Extracts year from release date provided by TMDb."""
    year = ''
    if release_date != None:
        year = release_date[:4]
    return year


def get_tmdb_mpaa_rating(response):
    """Extracts MPAA rating from response provided by TMDb."""
    results = response['release_dates']['results']
    rating = ''

    for result in results:
        if result['iso_3166_1'] == "US":
            rating = result['release_dates'][0]['certification']

    return rating


def TMDbSearchView(request):
    """Returns list of JSON search results from TMDb."""
    search_url = generate_tmdb_search_url(request.GET['query'])
    response = requests.get(search_url).json();

    results = []
    for movie in response.get('results'):
        movie_data = {
            'id': movie.get('id'),
            'title': movie.get('original_title'),
            'overview': movie.get('overview', ''),
            'release_year': truncate_tmdb_release_date(movie.get('release_date')),
            'poster_path': generate_tmdb_poster_path(movie.get('poster_path')),
        }
        results.append(movie_data)

    return JsonResponse(results, safe=False)


def TMDbDetailsView(request):
    """Returns JSON object with details of a specific movie from TMDb."""
    details_url = generate_tmdb_details_url(request.GET['query'])
    response = requests.get(details_url).json()
    movie_details = {
        'title': response.get('original_title'),
        'release_year': truncate_tmdb_release_date(response.get('release_date')),
        'mpaa_rating': get_tmdb_mpaa_rating(response),
        'runtime_minutes': response.get('runtime'),
        'image_link': generate_tmdb_poster_path(response.get('poster_path')),
    }

    return JsonResponse(movie_details)
