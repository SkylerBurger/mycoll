from django.contrib import admin
<<<<<<< HEAD
from django.urls import (
    include,
    path,
)
=======
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import HomePageView
>>>>>>> 0db35debfafee401ea853d4502b68880cd83582b


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
=======
    path('accounts/', include('accounts.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('movies/', include('movie_app.urls')),
>>>>>>> 0db35debfafee401ea853d4502b68880cd83582b
]
