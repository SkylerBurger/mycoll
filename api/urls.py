from django.urls import path, include

from movie_app.views import (
    MovieDetailView,
    MovieListView,
    MovieCopyDetailView,
    MovieCopyListView,
    TMDbDetailsView,
    TMDbSearchView,
) 


urlpatterns = [
    path('v1/movies/', include('movie_app.urls')),
    path('v1/tv/', include('tv_app.urls')),
]
