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


Chapter 09 - Intro to mixins
---------------------

If your classes have shared code you can put them into a "mixin".  This will allow you
to easily share code among multiple classes.

We will start by sharing the `login_required` requirement among both our classes, and
re-use this mixin in future classes we create.


Chapter 10 - Creating a form for new notes
-----------------------

Currently notes can only be created in the admin.  Add a new CBV (class-based view)
that allows note creation.

This also includes a new concept, forms.


Chapter 11 - Pagination
----------------------

If more than 5 forms are created then all the forms will not be displayed.  Add
pagination, and also make sure to sort the forms that we display by the date
they are published (in reverse order).


Chapter 12 - WYSIWYG
--------------------

Add in a more advanced editor.  A WYSIWYG (What You See Is What You Get) editor
will allow the text to be formatted.

Steps:

```
$ pip install django-wysiwyg==0.7.0
```

Diff between chapter 11 and 12 to see settings and template changes necessary.


Chapter 13 - Secure notes
-------------------

Currently anyone who is logged in can read any note (by modifying the URL).
Override the `get()` method to issue a 403 Forbidden if a user is trying to
read a note they don't own.


Chapter 14 - Editing existing notes
-------------------

Add the ability to edit existing notes, as well as a link from the index page
to the edit page.
