# MyColl Back End

## What is MyColl?

[MyColl](https://mycoll.app), pronounced 'Michael' but short for 'my collection', is a web app for cataloging your media collection. With MyColl you can search The Movie Database API to effortlessly add movies to your collection, then record any copies you may own along with its format and platform details. Now you'll know if your copy of Michael Chrichton's 1998 aquatic-horror thriller, Sphere, is a DVD sitting at home on your shelf, a VOD on a service like Amazon's Prime Video, or both! Currently the application supports movies but cataloging of shows and books will be integrated.

## Architecture:

### API

Check out the docs for MyColl's back-end API over on Postman!

[**MyColl API Documentation**](https://documenter.getpostman.com/view/6103333/T1Ds8ayi?version=latest)

### Frameworks, Packages, and Libraries
- [**Django**](https://www.djangoproject.com/): A Python framework for building web applications and servers
- [**`djangorestframework`**](https://www.django-rest-framework.org/): A package for quickly developing REST APIs with Django
- [**`djangorestframework-simplejwt`**](https://github.com/davesque/django-rest-framework-simplejwt): A package for enabling JSON Web Tokens for user auth
- [**`django-environ`**](https://github.com/joke2k/django-environ): A package for handling environment variables
- [**Docker** & **Docker-Compose**](https://www.docker.com/): A protocol for containerization, used during development only
- [**`pyscopg2-binary`**](https://github.com/psycopg/psycopg2): A package for allowing communication between Python and a PostgreSQL database
- [**`requests`**](https://2.python-requests.org/en/master/): A package for handling HTTP/HTTPS requests
- [**`whitenoise`**](https://github.com/evansd/whitenoise): A package for managing static files

### Models
- **Movie**: Models a unique film in your collection.
- **MovieCopy**: Models a specific copy of a film in your collection whether video-on-demand (VOD) or DVD.

### Full Stack Diagram

![MyColl Diagram](./staticfiles/mycoll_diagram.jpg)
    
## Roadmap
- Add Show model
- Add TMDb API integration for searching shows
- Add Book model
- Add Google Books API integration for searching books
