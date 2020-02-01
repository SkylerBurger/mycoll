from django.urls import path

from movie_app.views import (
    MovieDetailView,
    MovieListView,
    MovieCopyListView,
) 


urlpatterns = [
    path('v1/movies/', MovieListView.as_view(), name='movie_list'),
    path('v1/movies/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('v1/movies/copies/', MovieCopyListView.as_view(), name='movie_copy_list'),
]
