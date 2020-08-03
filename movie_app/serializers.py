from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
)

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


class MovieSerializer(AttributeOwnerMixin, ModelSerializer):
    class Meta:
        model = Movie
        # 'depth' sets the level of detail the serializer will show
        # before flattening the representation to an ID
        # 'depth = 1' will expand the detail of the related copies
        depth = 1
        fields = [
            'id',
            'title',
            'overview',
            'release_year',
            'mpaa_rating',
            'runtime_minutes',
            'image_link',
            'tmdb_page_link',
            'copies',  # Related Model
        ]


class MovieCopySerializer(AttributeOwnerMixin, ModelSerializer):
    class Meta:
        model = MovieCopy
        fields = [
            'id',
            'movie',
            'platform',
            'form',
            'vod_link',
        ]
