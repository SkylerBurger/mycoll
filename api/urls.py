from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from movie_app.views import (
    MovieListView,
    MovieCopyListView,
) 


urlpatterns = [
    path('v1/movies/', MovieListView.as_view(), name='movie_list'),
    path('v1/movies/copies/', MovieCopyListView.as_view(), name='movie_copy_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
