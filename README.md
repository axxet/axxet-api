Axxet
===============

Technology: 

* [Django Rest Framwork](http://www.django-rest-framework.org/)
* [AngularJS](https://angularjs.org/)
* [JSON Web Token JWT](https://auth0.com/blog/2014/01/07/angularjs-authentication-with-cookies-vs-token/) provided by [Django REST framework JWT Auth](https://github.com/GetBlimp/django-rest-framework-jwt)

## Installation

Please follow those steps: 

* install required Python modules: ```pip install -r requirements.txt```
* change directory: ```cd axxet```
* init Django application: ```python ./manage.py syncdb```, and create user (username: ```admin``` and password: ```abc123```)
* run application: ```python ./manage.py runserver``` (this serves application on localhost on port 8000)

## Run in browser

* run browser window
* open page ```http://localhost:8000/```, it shows home page
* open page ```http://localhost:8000/api```, it shows DRF API Root, please login (admin:abc123) to get access
* open page ```http://localhost:8000/admin```, it gets access to Django's admin pages

## API Examples

### Tokens

* Get token:
```curl -X POST -d "username=admin&password=abc123" http://localhost:8000/api-key/get/```
* Refresh token:
```curl -X POST -H "Content-Type: application/json" -d '{"token":"<EXISTING_TOKEN>"}' http://localhost:8000/api-key/refresh/```
* Verify token:
```curl -X POST -H "Content-Type: application/json" -d '{"token":"<EXISTING_TOKEN>"}' http://localhost:8000/api-key/verify/```

### Etc.

* Get users list:
```curl -H "Authorization: JWT <TOKEN>" http://localhost:8000/api/users/```

## Running pep8

- ```pep8 .```
- ```autopep8 --in-place --aggressive --aggressive <filename>```
