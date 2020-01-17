from django.urls import path

from .views import (
    MovieListView, 
    MovieCreateView, 
    MovieDetailView,
    MovieUpdateView,
    MovieDeleteView,
)


urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('create', MovieCreateView.as_view(), name='movie_create'),
    path('detail/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('update/<int:pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('delete/<int:pk>', MovieDeleteView.as_view(), name='movie_delete'),
]
