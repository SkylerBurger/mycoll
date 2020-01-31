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

"""
Create to this StackOverflow page for the create() method:
https://stackoverflow.com/questions/57827478/how-to-assign-a-logged-in-user-automatically-to-a-post-in-django-rest-framework
Discussion at bottom of the page helped me realize 
where I needed to insert the current user before creating an instance of a model.
I tried to further alter the default methods of the generic views 
and realized they were using the serializers to create new instances.
CDRF.co site helped me understand structure of the default create() method.
"""
