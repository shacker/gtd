# GTD: Container/stub site for django-todo

[Django-todo](https://github.com/shacker/django-todo) is a reusable app that can be plugged into any
running Django project. If you don't have a handy Django project to plug it into, or just want a
quick starter site to try django-todo in, this project is the reference / example host site used by
the author (though you might find it handy as a generic Django starter site for other purposes as
well).

## Installation

`clone` the repository and use `pipenv` to create the virtual environment and install the
dependencies. The instructions below assume you are using sqlite as your database, `~/dev` as your
development directory, and pipenv as your environment manager. Modify as needed.

```
pip3 install --user git+https://github.com/pypa/pipenv.git
cd ~/dev
git clone git@github.com:shacker/gtd.git
cd gtd
pipenv --python 3.9   # Initializes the virtual environment
pipenv install --dev  # Installs all dependencies
pipenv shell  # Activates the environment
```

Copy `local.example.py` to `local.py` and modify to match your local db credentials. In `local.py`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Then:

`./manage.py migrate`

See additional instructions in the django-todo README.

## Deploy via fabric

TK...
