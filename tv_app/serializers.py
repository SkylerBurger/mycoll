from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
)

from .models import (
    Show,
    Season,
    SeasonCopy,
)


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


class AttributeShowMixin:
    """Takes the show id from the form data and adds it to 'show_id' in validated data."""
    def create(self, validated_data):
        show_id = int(self.context['request'].POST['show'][0])
        validated_data['show_id'] = show_id

        return super().create(validated_data)


class ShowSerializer(AttributeOwnerMixin, ModelSerializer):
    class Meta:
        model = Show
        depth = 1  # Setting depth at 2 should show Seasons and SeasonCopys
        fields = [
            'id',
            'title',
            'year_first_aired',
            'overview',
            'image_link',
            'tmdb_page_link',
            'seasons',  # The related model
        ]


class SeasonSerializer(AttributeOwnerMixin, AttributeShowMixin, ModelSerializer):
    class Meta:
        model = Season
        depth = 1
        fields = [
            'id',
            'show',
            'title',
            'season_number',
            'episode_count',
            'year_first_aired',
            'overview',
            'image_link',
            'tmdb_page_link',
            'season_copies',
        ]


class SeasonCopySerializer(AttributeOwnerMixin, ModelSerializer):
    class Meta:
        model = SeasonCopy
        fields = [
            'id',
            'season',
            'platform',
            'form',
            'vod_link',
        ]