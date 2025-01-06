#!/bin/bash

set -ex

# apk update

[ -f "db.sqlite3" ] && rm db.sqlite3 || echo "No existing database found"

pip install -U pip pipenv

pipenv install

pipenv run ./manage.py migrate
pipenv run ./manage.py createsuperuser --noinput
pipenv run ./manage.py loaddata api/fixtures/example_tasks.json --app api.Task
pipenv run ./manage.py runserver 0.0.0.0:8100

/bin/sh