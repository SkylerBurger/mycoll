from django.urls import path

from .views import (
    MovieDetailView,
    MovieListView,
    MovieCopyDetailView,
    MovieCopyListView,
    TMDbDetailsView,
    TMDbSearchView,
) 


urlpatterns = [
    path('', MovieListView.as_view(), name = 'movie_list'),
    path('<int:pk>', MovieDetailView.as_view(), name = 'movie_detail'),
    path('copies/', MovieCopyListView.as_view(), name = 'movie_copy_list'),
    path('copies/<int:pk>', MovieCopyDetailView.as_view(), name = 'movie_copy_detail'),
    path('search',TMDbSearchView,name = 'tmdb_movie_search'),
    path('search/details',TMDbDetailsView,name = 'tmdb_movie_details'),
]
