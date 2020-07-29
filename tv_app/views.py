from django.contrib.auth.models import AnonymousUser

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    Show,
    Season,
    SeasonCopy,
)
from .serializers import (
    ShowSerializer,
    SeasonSerializer,
    SeasonCopySerializer,
)


# ============
# CLASS MIXINS
# ============

class MyShowsMixin:
    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user = self.request.user
            return Show.objects.all().filter(owner=user)
        else:
            return None


class MySeasonsMixin:
    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user = self.request.user
            return Season.objects.all().filter(owner=user)
        else:
            return None


class MySeasonCopiesMixin:
    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user = self.request.user
            return SeasonCopy.objects.all().filter(owner=user)
        else:
            return None


# =====
# VIEWS
# =====

class ShowDetailView(MyShowsMixin, RetrieveUpdateDestroyAPIView):
    model = Show
    serializer_class = ShowSerializer


class ShowListView(MyShowsMixin, ListCreateAPIView):
    model = Show
    serializer_class = ShowSerializer


class SeasonDetailView(MySeasonsMixin, RetrieveUpdateDestroyAPIView):
    model = Season
    serializer_class = SeasonSerializer


class SeasonCopyDetailView(MySeasonCopiesMixin, RetrieveUpdateDestroyAPIView):
    model = SeasonCopy
    serializer_class = SeasonCopySerializer


# ================
# HELPER FUNCTIONS
# ================
