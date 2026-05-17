# GTD: Container/stub site for django-todo

[Django-todo](https://github.com/shacker/django-todo) is a reusable app that can be plugged into any
running Django project. If you don't have a handy Django project to plug it into, or just want a
quick starter site to try django-todo in, this project is the reference / example host site used by
the author (though you might find it handy as a generic Django starter site for other purposes as
well).

## Installation

Requires [uv](https://docs.astral.sh/uv/). Clone the repo, then:

```
cd ~/dev
git clone git@github.com:shacker/gtd.git
cd gtd
uv sync
```

Copy `project/local.example.py` to `project/local.py` and update with your local db credentials
and a `SECRET_KEY`. Then:

```
createdb gtd
uv run manage.py migrate
uv run manage.py createsuperuser
uv run manage.py runserver
```

See additional instructions in the django-todo README.


## Local django-todo development

`pyproject.toml` points `django-todo` at a local editable install (`../django-todo`) via
`[tool.uv.sources]`. This lets you work on the library and see changes reflected immediately.

On the server, bypass the local source and install from PyPI instead:

```
uv sync --no-sources
```


## Dependencies

Dependencies are declared in `pyproject.toml` and locked in `uv.lock`. To add or remove packages:

```
uv add <package>
uv remove <package>
```

To upgrade all packages to their latest allowed versions:

```
uv lock --upgrade
uv sync
```