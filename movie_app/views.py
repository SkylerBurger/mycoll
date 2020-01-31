from django.contrib.auth.models import AnonymousUser

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


class MovieListView(ListCreateAPIView):
    model = Movie
    serializer_class = MovieSerializer

    def get_queryset(self):
        print('*** DEF GET_QUERYSET USER:',self.request.user)
        if not isinstance(self.request.user, AnonymousUser):
            user = self.request.user
            return Movie.objects.all().filter(owner=user)
        else:
            return None


class MovieCopyListView(ListCreateAPIView):
    model = MovieCopy
    serializer_class = MovieCopySerializer

    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user = self.request.user
            return MovieCopy.objects.all().filter(owner=user)
        else:
            return None
    
