from rest_framework import serializers

from .models import Movie, MovieCopy


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'release_year',
            'mpaa_rating',
            'run_time_minutes',
        ]


class MovieCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCopy
        fields = [
            'owner',
            'movie',
            'platform',
            'form',
        ]
