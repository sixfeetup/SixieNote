# SixieNote in Django 

Uses:
* Django 3.0
* Python 3.8

## Getting Started using Docker

Clone this repository and you can start developing on the project using the
following commands.

```console
$ cp docker-compose.override.yml.example docker-compose.override.yml
$ make build-dev
$ docker-compose up
```

This will give you a running Postgres, Mailhog and a Django running under
`runserver_plus` at http://localhost:8000. Start editing your code!

## Getting Started with a Local Virtualenv

Clone the repo like above, but you will be responsible for setting up the
database, a database user and the mailhog instance. You will also need to make
sure you have Python 3.8 installed and use it to create your `virtualenv`.

Once you have all of that, you need to install the requirements files in the
`requirements/` folder for your specific situation (local dev or production).

On second thought, let's just make it easy on ourselves and the Docker way
above.
