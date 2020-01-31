# MyColl
A back-end API written in Django for a media collection application.

## Architecture:
- [**Django**](https://www.djangoproject.com/)
- [**Django REST Framework**](https://www.django-rest-framework.org/)
- [**Django REST Framework SimpleJWT**](https://github.com/davesque/django-rest-framework-simplejwt)
- [**Gunicorn**](https://gunicorn.org/)

## Models
- **Movie**: Models a unique film in your collection.
- **MovieCopy**: Models a specific copy of a film in your collection whether video-on-demand (VOD) or DVD.

## API
- **api/v1/**
  - **movies/**: A list view of all of the movies in your collection
  - **movies/copies/**: A list view of all of the movie copies in your collection