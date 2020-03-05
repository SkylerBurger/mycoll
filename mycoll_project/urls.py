from django.contrib import admin
from django.urls import (
    include,
    path,
)

from .views import react


urlpatterns = [
    path(
        '',
        react,
        name='react'
    ),
    path(
        'accounts/', 
        include('accounts.urls'),
    ),
    path(
        'admin/', 
        admin.site.urls,
    ),
    path(
        'api/', 
        include('api.urls'),
    ),
    path(
        'api-auth/', 
        include('rest_framework.urls'),
    ),
]
