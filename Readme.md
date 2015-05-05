ElevenNote in Django 
====================

Uses:
* Django 1.8.1
* Python 3.4

Chapter 01 - Create the project
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

Create a superuser:
```
$ python manage.py createsuperuser
...
$ python manage.py runserver
```

Connect to the admin at http://localhost:8000/admin


Chapter 02 - Create a new app
----------

Make your app:

```
$ python manage.py startapp note
```

Modify models.py and admin.py to contain your first model.

Apply changes to DB:
```
$ ./manage.py makemigrations note
$ ./manage.py migrate
```

You can now view this in the admin.


Chapter 03 - Customize the admin
----------

Modify the `note/admin.py` file and see how the admin can be customized.


Chapter 04 - Make the first views
----------

Modify `note/urls.py`, `note/views.py`, and `elevennote/settings.py` to 
and create templates in the `note/templates/note/...` directory to create
your first views.


Chapter 05 - Authentication
--------------------------

Add URLs and templates for the authentication system.  Make the existing
views use the `@login_required` decorator.

(Also, add in a redirect for the root URL)


Chapter 06 - Better templates and new users
-----------------------------

Copy in templates and add in urls for creating new users.


Chapter 07 - Associating notes with owners
-------------------------

Add an `owner` field to the model.  You'll need to run migrations.  You can use
a default value of 0 for the migration.

```
$ ./manage.py makemigrations note
$ ./manage.py migrate
```

Then, restrict the view on the index page so that a user can only see their own notes.


Chapter 08 - Switch to CBVs
-------------------

Class-based views can significantly reduce code.  Switch our two function-based views
to class-based views before we begin adding more views.
