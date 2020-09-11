from django.db import models
from django.urls import reverse


class Show(models.Model):
    owner = models.ForeignKey('auth.user', related_name='shows', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=200)
    year_first_aired = models.IntegerField('First Aired')
    overview = models.TextField('Overview', blank=True, null=True)
    image_link = models.CharField('Image Link', max_length=200, blank=True, null=True)
    tmdb_page_link = models.CharField('TDMb Page Link', max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.title} ({self.year_first_aired})'

    @property
    def _absolute_url(self):
        return reverse('show_detail', args=[str(self.id)])


class Season(models.Model):
    owner = models.ForeignKey('auth.user', related_name='all_seasons', on_delete=models.CASCADE)
    show = models.ForeignKey(Show, related_name='seasons', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=200, blank=True, null=True)
    season_number = models.IntegerField('Season Number')
    episode_count = models.IntegerField('Episode Count')
    year_first_aired = models.IntegerField('First Aired')
    overview = models.TextField('Overview', blank=True, null=True)
    image_link = models.CharField('Image Link', max_length=200, blank=True, null= True)
    tmdb_page_link = models.CharField('TMDb Page Link', max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.show.title} - Season {self.season_number}'

    @property
    def _absolute_url(self):
        return reverse('season_detail', args=[str(self.id)])

class SeasonCopy(models.Model):
    owner = models.ForeignKey('auth.user', related_name='all_season_copies', on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name='season_copies', on_delete=models.CASCADE)
    platform = models.CharField('Platform', max_length=200)
    form = models.CharField('Format', max_length=200)
    vod_link = models.CharField('VOD Link', max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.season.owner.username}\'s {self.form} of \
            {self.season.show.title} season {self.season.season_number} on {self.platform}'

    @property
    def _absolute_url(self):
        return reverse('season_copy_detail', args=[str(self.id)])