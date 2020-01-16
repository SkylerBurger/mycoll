from django.db import models
from django.urls import reverse


class Book(models.Model):
    owner = models.ForeignKey(
        'auth.user', 
        related_name='books', 
        on_delete=models.CASCADE,
    )
    title = models.CharField('title', max_length=200)
    author = models.CharField('author(s)', max_length=200)
    published = models.IntegerField('published')

    def __str__(self):
        return f'{self.owner.username} - {self.title} by {self.author}'

    # This method allows for redirect upon creation
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
    

class BookCopy(models.Model):
    book = models.ForeignKey(
        Book, 
        related_name='copies', 
        on_delete=models.CASCADE,
    )
    platform = models.CharField('platform', max_length=200)
    form = models.CharField('format', max_length=200)

    def __str__(self):
        return f'{self.book.owner.username}\'s {self.form} copy of {self.book.title} on {self.platform}'

    def get_absolute_url(self):
        return reverse("book_copy_detail", args=[str(self.id)])