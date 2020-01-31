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
            'runtime_minutes',
        ]
    
    def create(self, validated_data):
        """
        Overrides default create() method
        to add user utilizing JWT
        """
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class MovieCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCopy
        fields = [
            'id',
            'movie',
            'platform',
            'form',
        ]

    def create(self, validated_data):
        """
        Overrides default create() method
        to add user utilizing JWT
        """
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
