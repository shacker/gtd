# GTD: Container/stub site for django-todo

[Django-todo](https://github.com/shacker/django-todo) is a reusable app that can be plugged into any
running Django project. If you don't have a handy Django project to plug it into, or just want a
quick starter site to try django-todo in, this project is the reference / example host site used by
the author (though you might find it handy as a generic Django starter site for other purposes as
well).

## Installation

`clone` the repository and use `pipenv` to create the virtual environment and install the
dependencies. The instructions below assume you are using sqlite as your database, `~/dev` as your
development directory, and venv as your environment manager. Modify as needed.

```
cd ~/dev
git clone git@github.com:shacker/gtd.git
cd gtd
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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


## Dependencies

To add, remove, or change the project's Python dependencies, edit `base.in`, then recompile
requirements.txt for the changed package:

```
pip-compile --generate-hashes --output-file=requirements.txt -P <package-name> requirements/base.in
```

(specify `-P <package_name>`)

ie. to update to a newer Django version, edit base.in, then:

```
pip-compile --generate-hashes --output-file=requirements.txt -P django base.in
```

To generate new/fresh hash files, delete both .txt files then run the commands without specifying a package:

```
pip-compile --generate-hashes --verbose --output-file=requirements.txt base.in
```