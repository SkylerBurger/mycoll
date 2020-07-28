from django.contrib import admin

from .models import (
    Show,
    Season,
    SeasonCopy,
)

admin.site.register([
    Show,
    Season,
    SeasonCopy,
])