from rest_framework import serializers

from .models import Movie, MovieCopy


class AttributeOwnerMixin:
    """
    Inserts the user's ID as the owner property when creating new instances.
    """
    def create(self, validated_data):
        """
        Overrides default create() method to add ID of a user utilizing JWT
        Credit to:
        https://stackoverflow.com/questions/57827478/how-to-assign-a-logged-in-user-automatically-to-a-post-in-django-rest-framework
        """
        validated_data['owner'] = self.context['request'].user

        return super().create(validated_data)


class MovieSerializer(AttributeOwnerMixin, serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'release_year',
            'mpaa_rating',
            'runtime_minutes',
        ]


class MovieCopySerializer(AttributeOwnerMixin, serializers.ModelSerializer):
    class Meta:
        model = MovieCopy
        fields = [
            'id',
            'movie',
            'platform',
            'form',
        ]
