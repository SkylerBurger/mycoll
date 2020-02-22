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
    base_url = 'https://api.themoviedb.org/3/search/movie'
    # TODO: Remove the api key from this file and place into a .env file
    api_key = '?api_key=' + '067c757c5122bd33acc966e32828544c'
    query_param = '&query=' + query

    return base_url + api_key + query_param


def generate_tmdb_poster_path(path):
    poster_path_url = ''
    base_url = 'https://image.tmdb.org/t/p/w500'
    
    if path != None:
        poster_path_url = base_url + path
    
    return poster_path_url


def TMDbSearchView(request):
    search_url = generate_tmdb_search_url(request.GET['query'])
    response = requests.get(search_url).json();

    results = []
    for movie in response.get('results'):
        print("MOVIE", movie)
        movie_data = {}
        movie_data['title'] = movie['original_title']
        movie_data['poster_path'] = generate_tmdb_poster_path(movie.get('poster_path'))
        # movie_data.overview = movie.overview
        # movie_data.id = movie.id
        results.append(movie_data)

    print(results)

    return JsonResponse(response)
