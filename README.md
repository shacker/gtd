# gtd

Container/stub site for django-todo

## Installation

First `clone` the repository and use `pipenv` to create 
the virtual environment and install the dependencies.


If you want to test the site locally, make sure that 
before `migrate`, you create a file called `local.py` inside 
project directory and set the parameters following the
example of `local.example.py`.

For a basic database configuration, use:

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}`
