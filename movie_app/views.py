from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions

from .models import Movie
from .serializers import MovieSerializer
from.permissions import IsOwnerOrReadOnly


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_app/movie_detail.html'
    content_object_name = 'movie'


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_app/movie_list.html'
    context_object_name = 'movie_list'


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movie_app/movie_create.html'
    fields = ['title', 'release_year', 'mpaa_rating', 'run_time_minutes']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(MovieCreateView, self).form_valid(form)


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movie_app/movie_update.html'
    fields = ['title', 'release_year', 'mpaa_rating', 'run_time_minutes']


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_app/movie_delete.html'
    success_url = reverse_lazy('home')



# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer 


class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer 
