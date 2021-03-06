from django.urls import (
    include,
    path,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserCreateView


urlpatterns = [
    path(
        '', 
        include('django.contrib.auth.urls')
    ),
    path(
        'create/', 
        UserCreateView.as_view(), 
        name = 'account_create'
    ),
    path(
        'token/', 
        TokenObtainPairView.as_view(), 
        name = 'token_obtain_pair'
    ),
    path(
        'token/refresh/', 
        TokenRefreshView.as_view(), 
        name = 'token_refresh'
    ),
]
