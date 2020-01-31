from django.urls import include, path
from rest_framework import routers

from movie_app.views import MovieListAPIView, MovieCopyListAPIView, MovieCopyRUDView


urlpatterns = [
    path('movies/', MovieListAPIView.as_view()),
    path('movies/copies/', MovieCopyListAPIView.as_view()),
    path('movies/copies/<int:pk>/', MovieCopyRUDView.as_view()),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]