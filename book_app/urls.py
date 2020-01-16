from django.urls import path

from .views import (
    BookListView, 
    BookDetailView, 
    BookCreateView,
    BookDeleteView, 
    BookCopyCreateView, 
    BookCopyDetailView,
)


urlpatterns = [
    path('', BookListView.as_view(), name='books'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book_create', BookCreateView.as_view(), name='book_create'),
    path('book_delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('copy_create/<int:pk>', BookCopyCreateView.as_view(), name='book_copy_create'),
    path('copy_detail/<int:pk>', BookCopyDetailView.as_view(), name='book_copy_detail'),
]
