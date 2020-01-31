from django.urls import reverse_lazy
from django.contrib.auth.models import AnonymousUser
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from rest_framework import generics
from rest_framework import permissions

from .models import Movie, MovieCopy
from .serializers import MovieSerializer, MovieCopySerializer
from .permissions import IsOwner


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
    serializer_class = MovieSerializer 


class MovieListAPIView(generics.ListAPIView):
    Model = Movie
    permission_classes = [
        IsOwner,
    ]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    # def get_queryset(self):
    #     if not isinstance(self.request.user, AnonymousUser):
    #         user = self.request.user
    #         print(user)
    #         return Movie.objects.all().filter(owner=user)
    #     else:
    #         return None


class MovieCopyListAPIView(generics.ListAPIView):
    model = MovieCopy
    permission_classes = [
        IsOwner,
    ]  
    serializer_class = MovieCopySerializer
    queryset = MovieCopy.objects.all()

    def get_queryset(self):
        user = self.request.user
        return MovieCopy.objects.all().filter(owner=user)


class MovieCopyRUDView(generics.RetrieveUpdateDestroyAPIView):
    model = MovieCopy
    permission_classes = [
        IsOwner,
    ]
    serializer_class = MovieCopySerializer
    queryset = MovieCopy.objects.all()


# Next Step:
# - package my custom get_queryset into an OPP mixin class
