from django.contrib import admin
from .models import Book, BookCopy

admin.site.register(Book)
admin.site.register(BookCopy)
