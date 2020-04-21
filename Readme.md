SixieNote in Django 
====================

Uses:
* Django 3.0
* Python 3.8

See the wiki (on github) for details on each chapter.  Below is just an
overview.

Chapter 01 - Create the project
----------

Make the project:

```
$ django-admin startproject sixienote
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

The way that the objects are listed can be modified as well as the fields
on the object's create/edit page.  Additionally, restrictions can be made
here (such as not allowing object deletion via the admin).

Chapter 04 - Make the first views
----------

Views are placed into `note/views.py`.  After creating views they need to
be added into `note/urls.py`.

The top level `urls.py` file needs an entry for our app as well.

Create templates in the `note/templates/note/` directory to create
your first views.  We'll start with really basic templates and then do
more with templating in future chapters.



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

If more than 5 forms are created then all the forms will not be displayed because
we have pagination enabled in the view.  But our template does not currently
support pagination.  Add pagination into the template, and also make sure to sort
the forms that we display by the date they are published (in reverse order).


Chapter 12 - WYSIWYG
--------------------

Add in a more advanced editor.  A WYSIWYG (What You See Is What You Get) editor
will allow the text to be formatted.

Steps:

```
$ pip install django-wysiwyg==0.7.0
```

Diff between chapter 11 and 12 to see settings and template changes necessary,
as well as the CKEditor downloaded from here:
http://download.cksource.com/CKEditor/CKEditor/CKEditor%204.4.7/ckeditor_4.4.7_basic.zip


Chapter 13 - Secure notes
-------------------

Currently anyone who is logged in can read any note (by modifying the URL).
Override the `get()` method to issue a 403 Forbidden if a user is trying to
read a note they don't own.


Chapter 14 - Editing existing notes
-------------------

Add the ability to edit existing notes, as well as a link from the index page
to the edit page.


Chapter 15 - Begin improving UI
----------------------

Begin improving	the UI by displaying the full note on the index	page.
Remove the edit	button.	 Instead, clicking on the name takes you to edit
the note.  (The	details	page isn't really needed any more)


Chapter 16 - Further improving UI
----------------------

Separate the form page into two columns.  The list of notes and a form
to create/edit a note.

We will do away with the index and detail views as they are no longer
used.


Chapter 16a - Add note deletion
-------------------

There is currently no way to delete a note except in the admin.
Add the ability to delete a note using a `DeleteView` CBV.
Make sure to protect against users deleting notes they do not own.


Chapter 17 - Building an API
-------------

Build a JSON endpoint to return the list of notes for a user.

Note: this code is not merged back to `master` because we will replace
this API with a better one built using Tastypie in the next chapter.


Chapter 18 - Building an API w/ Tastypie
-------------------

The version of Tastypie that pip will find by default is not new enough for Django
1.8, so install the latest version from Github:

```
pip install -e git+https://github.com/django-tastypie/django-tastypie#egg=TastyPie
```

Tastypie offers an easy way to build an API:
https://django-tastypie.readthedocs.org/en/latest/

http://localhost:8000/api/v1/note/schema/?format=json
http://localhost:8000/api/v1/note/?format=json

Note: in order to make the API more interesting we have loosened the restriction
here that prevents seeing other users posts.  (For that matter, our API is wide
open.  Anyone can access the data, even people who are not authenticated.  We
will get to that later.)


Chapter 19 - Adding users and filters to the API
------------------

We can add in filtering of the API with just a few lines of code.

We'll also add in users at the same time, and then this type of
filtering will work (swap [USERNAME] with `scot` or whatever):

http://localhost:8000/api/v1/note/?format=json&owner__username=[USERNAME]

You can also now see users info at:

http://localhost:8000/api/v1/user/schema/?format=json
http://localhost:8000/api/v1/user/?format=json

Note how we restricted some user fields.  We don't want to make the users
emails (and other fields) publicly accessible.


Chapter 20 - API - authentication and authorization
----------------------

Revisit the issue of locking down the API so that a user can only see
their own notes.

This users Django authentication and a custom authorization model.

http://localhost:8000/api/v1/note/?format=json&owner__username=[NOT YOU!]


Chapter 21 - API - authentication with a token
--------------------

Configure Tastypie to use API keys.  Add in a profile to display the user's
API key to them.

We'll put in a hook that makes a new API key for each new user, but to
create keys for all the users who already exist run this command:

```
# Run migrate again because Tastypie needs to make a DB table to hold the keys
$ python manage.py migrate
$ python manage.py backfill_api_keys
```

In order to view your API key make use of the profile link in the top right.  Create
a new view using TemplateView and fetch the `api_key` in the `get_context_data` and
pass it to the template to display.

Once you know your API key you can use your browser like so:
http://localhost:8000/api/v1/note/?format=json&username=a&api_key=416d65381bcfb395ae7312c8028b7650b3413594

or the command like like so:

```
$ curl --dump-header - -H "Authorization: ApiKey a:416d65381bcfb395ae7312c8028b7650b3413594" http://localhost:8000/api/v1/note/?format=json
```


Chapter 22 - Changing passwords
-------------------------

On the profile page, add the ability to change the user's password.


Chapter 23 - Settings info and debug toolbar
------------------------

Work with the settings file and try out the useful debug toolbar.
