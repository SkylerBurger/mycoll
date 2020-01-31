from django.contrib import admin

from .models import Movie, MovieCopy


admin.site.register([
    Movie, MovieCopy
])
