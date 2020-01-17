from django.urls import include, path
from rest_framework import routers

from movie_app.views import MovieViewSet


router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]