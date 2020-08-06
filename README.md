# MyColl Back End

## What is MyColl?

[MyColl](https://mycoll.app) is a web app for cataloging your media collection. With MyColl you can search The Movie Database API to effortlessly add movies to your collection, then record any copies you may own along with its format and platform details. Now you'll know if your copy of Michael Chrichton's 1998 aquatic-horror thriller, Sphere, is a DVD sitting at home on your shelf, a VOD on a service like Amazon's Prime Video, or both!

## Architecture:

### Frameworks, Packages, and Libraries
- [**Django**](https://www.djangoproject.com/): A Python framework for building web applications and servers
- [**`djangorestframework`**](https://www.django-rest-framework.org/): A package for quickly developing REST APIs with Django
- [**`djangorestframework-simplejwt`**](https://github.com/davesque/django-rest-framework-simplejwt): A package for enabling JSON Web Tokens for user auth
- [**`django-environ`**](https://github.com/joke2k/django-environ): A package for handling environment variables
- [**Docker** & **Docker-Compose**](https://www.docker.com/): A protocol for containerization, used during development only
- [**`pyscopg2-binary`**](https://github.com/psycopg/psycopg2): A package for allowing communication between Python and a PostgreSQL database
- [**`requests`**](https://2.python-requests.org/en/master/): A package for handling HTTP/HTTPS requests
- [**`whitenoise`**](https://github.com/evansd/whitenoise): A package for managing static files

### API

The deployed API on [db.mycoll.app](https://db.mycoll.app/) currently includes the Movie and MovieCopy models. This GitHub repository includes those models in addition to Show, Season, and SeasonCopy.

#### Documentation

Check out the docs for MyColl's back-end API over on Postman! --> [MyColl API Documentation](https://documenter.getpostman.com/view/6103333/T1Ds8ayi?version=latest)


#### Entity Relationship Diagram

<div style="width: 640px; height: 480px; margin: 10px; position: relative;"><iframe allowfullscreen frameborder="0" style="width:640px; height:480px" src="https://app.lucidchart.com/documents/embeddedchart/89529833-6f1f-491e-bba6-a42d9dafa1ca" id="Lt_jFqzyvUpc"></iframe></div>


### Full Stack Diagram

![MyColl Diagram](./staticfiles/mycoll_diagram.jpg)
