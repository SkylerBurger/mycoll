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
<<<<<<< HEAD
            'runtime_minutes',
        ]
    
    def create(self, validated_data):
        """
        Overrides default create() method
        to add user utilizing JWT
        """
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
=======
            'run_time_minutes',
        ]
>>>>>>> 0db35debfafee401ea853d4502b68880cd83582b


class MovieCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCopy
        fields = [
<<<<<<< HEAD
            'id',
=======
            'owner',
>>>>>>> 0db35debfafee401ea853d4502b68880cd83582b
            'movie',
            'platform',
            'form',
        ]
<<<<<<< HEAD

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
=======
>>>>>>> 0db35debfafee401ea853d4502b68880cd83582b
