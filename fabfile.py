# Update django-todo.org with latest "shell site" and dependencies
# (most importantly django-todo). Migrate, collecstatic, then restart
# gunicorn and nginx.

from fabric.contrib.files import exists
from fabric.api import cd, env, run, sudo
from fabric.utils import abort

REPO_URL = "https://github.com/shacker/gtd.git"
SITE_DIR = "/home/django/gtd"
env.user = "django"
env.hosts = ["django-todo.org"]


def deploy():
    """Call typical Django site deployment steps in order."""

    with cd(SITE_DIR):
        _update_source()
        _update_virtualenv()
        _update_static_files()
        _update_database()
        _restart_servers()


def _update_source():
    if exists(".git"):
        run("git checkout master")
        run("git pull origin master")
    else:
        current_dir = run("pwd")
        abort(f"{current_dir} does not appear to be a git directory. Exiting.")


def _update_virtualenv():
    run('pipenv install')


def _update_static_files():
    run("pipenv run ./manage.py collectstatic --noinput")


def _update_database():
    run("pipenv run ./manage.py migrate")


def _restart_servers():
    sudo("systemctl restart gunicorn")
    sudo("service nginx restart")
