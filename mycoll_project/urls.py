from django.contrib import admin
from django.urls import path, include

from .views import HomePageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('api/', include('api.urls')),
    path('movies/', include('movie_app.urls')),
]
