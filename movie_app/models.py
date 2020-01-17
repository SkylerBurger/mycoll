from django.db import models
from django.urls import reverse


class Movie(models.Model):
    owner = models.ForeignKey('auth.user', related_name='movies', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=200)
    release_year = models.IntegerField('Release Year')
    mpaa_rating = models.CharField('MPAA Rating', max_length=4)
    run_time_minutes = models.IntegerField('Run Time (mins)')

    def __str__(self):
        return f'{self.title} ({self.release_year})'

    def get_absolute_url(self):
        return reverse("movie_detail", args=[self.id])
