#!/bin/bash

set -ex

num_tasks=${1:-0}
if [[ -z "$num_tasks" || ! "$num_tasks" =~ ^[0-9]+$ ]]; then
	echo "Usage: $0 <number of tasks to generate>"
	exit 1
fi

[ -f "db.sqlite3" ] && rm db.sqlite3 || echo "No existing database found"

pip install -U pip pipenv

pipenv install --dev

pipenv run ./manage.py migrate
pipenv run ./manage.py createsuperuser --noinput
pipenv run ./manage.py create_random_tasks $num_tasks
pipenv run ./manage.py runserver 0.0.0.0:8100

/bin/sh