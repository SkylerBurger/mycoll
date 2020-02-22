from django.urls import path

from movie_app.views import (
    MovieDetailView,
    MovieListView,
    MovieCopyDetailView,
    MovieCopyListView,
    TMDbDetailsView,
    TMDbSearchView,
) 


urlpatterns = [
    path(
        'v1/movies/', 
        MovieListView.as_view(), 
        name = 'movie_list'
    ),
    path(
        'v1/movies/<int:pk>', 
        MovieDetailView.as_view(), 
        name = 'movie_detail'
    ),
    path(
        'v1/movies/copies/', 
        MovieCopyListView.as_view(), 
        name = 'movie_copy_list'
    ),
    path(
        'v1/movies/copies/<int:pk>', 
        MovieCopyDetailView.as_view(), 
        name = 'movie_copy_detail'
    ),
    path(
        'v1/movies/search',
        TMDbSearchView,
        name = 'tmdb_movie_search'
    ),
    path(
        'v1/movies/search/details',
        TMDbDetailsView,
        name = 'tmdb_movie_details'
    ),
]
