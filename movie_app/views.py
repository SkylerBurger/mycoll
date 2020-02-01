from django.contrib.auth.models import AnonymousUser

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    Movie, 
    MovieCopy,
)
from .permissions import IsOwner
from .serializers import (
    MovieSerializer,
    MovieCopySerializer,
)


class MyMovieMixin:
    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user = self.request.user
            return Movie.objects.all().filter(owner=user)
        else:
            return None


class MyMovieCopyMixin:
    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user = self.request.user
            return MovieCopy.objects.all().filter(owner=user)
        else:
            return None


class MovieDetailView(MyMovieMixin, RetrieveUpdateDestroyAPIView):
    model = Movie
    serializer_class = MovieSerializer


class MovieListView(MyMovieMixin, ListCreateAPIView):
    model = Movie
    serializer_class = MovieSerializer


class MovieCopyListView(MyMovieCopyMixin, ListCreateAPIView):
    model = MovieCopy
    serializer_class = MovieCopySerializer

