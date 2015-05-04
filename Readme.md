ElevenNote in Django 
====================

Uses:
* Django 1.8.1
* Python 3.4

Chapter 01
----------

Make the project:

```
$ django-admin startproject elevennote
```

Create some initial tables:
```
$ python manage.py migrate
```

Run the server:
```
$ python manage.py runserver
```

And connect at http://localhost:8000/ to verify that everything is working.

Chapter 02
----------

Make your app:

```
$ python manage.py startapp note
```


