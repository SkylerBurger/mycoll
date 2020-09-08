from django.db import models
from django.urls import reverse


class Movie(models.Model):
    owner = models.ForeignKey('auth.user', related_name='movies', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=200)
    release_year = models.IntegerField('Release Year')
    overview = models.TextField('Overview', blank=True, null=True)
    mpaa_rating = models.CharField('MPAA Rating', max_length=5)
    runtime_minutes = models.IntegerField('Runtime (mins)')
    image_link = models.CharField('Image Link', max_length=200, blank=True, null=True)
    tmdb_page_link = models.CharField('TMDB Page Link', max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.title} ({self.release_year})'

    @property
    def _absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])

class MovieCopy(models.Model):
    movie = models.ForeignKey(Movie, related_name='copies', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.user', related_name='all_copies', on_delete=models.CASCADE)
    platform = models.CharField('Platform', max_length=200)
    form = models.CharField('Format', max_length=200)
    vod_link = models.CharField('VOD Link', max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.movie.owner.username}\'s {self.form} of {self.movie.title} on {self.platform}'

    @property
    def _absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])