from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Book, BookCopy


class BookListView(ListView):
    model = Book
    template_name = 'book_app/book_list.html'
    context_object_name = 'book_list'


class BookDetailView(DetailView):
    model= Book
    template_name = 'book_app/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_app/book_create.html'
    fields = ['title', 'author', 'published']

    # Credit to: 
    # https://stackoverflow.com/questions/10382838/how-to-set-foreignkey-in-createview/10565744#10565744 
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookCreateView, self).form_valid(form)

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_app/book_delete.html'
    success_url = reverse_lazy('book_list')


class BookCopyCreateView(CreateView):
    model = BookCopy
    template_name = 'book_app/book_copy_create.html'
    fields = ['platform', 'form']

    def form_valid(self, form):
        # Strip the Book ID from the referral URL
        book_id = self.request.META['HTTP_REFERER']
        # This is crude and may need to change
        # if the shape of the URL changes in the future
        book_id = book_id.split('/')[-1]
        
        # Set form's initial value for book to the book instance
        form.instance.book = Book.objects.get(pk=book_id)
        return super(BookCopyCreateView, self).form_valid(form)


class BookCopyDetailView(DetailView):
    model= BookCopy
    template_name = 'book_app/book_copy_detail.html'
    context_object_name = 'copy'