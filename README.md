# MyColl
A back-end API written in Django for a media collection application.

## Architecture:
- [**Django**](https://www.djangoproject.com/)
- [**Django REST Framework**](https://www.django-rest-framework.org/)
- [**Django REST Framework SimpleJWT**](https://github.com/davesque/django-rest-framework-simplejwt)

## Models
- **Movie**: Models a unique film in your collection.
- **MovieCopy**: Models a specific copy of a film in your collection whether video-on-demand (VOD) or DVD.

## API
- **accounts/**
  - **create/**
    - **POST**: Create a new user and receive a JWT pair to authenticate further requests
  - **token/**
    - **POST**: Submit login credentials to receive a JWT pair to authenticate further requests
  - **token/refresh/**
    - **POST**: Submit a refresh token to receive a new access token to authenticate further requests
- **api/v1/**
  - **movies/**
    - **GET**: A list view of all of the movies in your collection
    - **POST**: Add a new movie to your collection
  - **movies/\<id>**
    - **GET**: A detail view of a specific movie in your collection
    - **PUT**: Update the details of a specific movie in your collection
    - **DELETE**: Delete a movie and its related copies from your collection
  - **movies/copies/**
    - **GET**: A list view of all of the movie copies in your collection
    - **POST**: Add a new copy of a movie to your collection
  - **movies/copies/\<id>**
    - **GET**: A detail view of a specific copy of a movie in your collection
    - **PUT**: Update the details of a specific copy of a movie in your collection
    - **DELETE**: Delete a specific copy of a movie from your collection
    
## Roadmap
Please refer to my Trello board for updates: [MyColl Trello Board](https://trello.com/b/z3woB4Z3/mycoll)
