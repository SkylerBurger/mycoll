from django.urls import (
    include,
    path,
)

from .views import UserCreateView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('create/', UserCreateView.as_view(), name='account_create'),
]
