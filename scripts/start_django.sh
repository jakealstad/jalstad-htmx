#!/bin/bash

set -ex

# apk update

pip install -U pip pipenv

pipenv install
# pipenv run ./manage.py migrate
# pipenv run ./manage.py runserver 0.0.0.0:8100

/bin/sh