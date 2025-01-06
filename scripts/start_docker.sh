#!/bin/bash

projectdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."
cd $projectdir

  docker run \
    --init \
    -it \
    --rm \
    --name htmx-test \
    --entrypoint /bin/sh \
    --dns 1.1.1.1 \
    -v $projectdir:/application \
    -w /application \
    --env DJANGO_SUPERUSER_USERNAME=admin \
    --env DJANGO_SUPERUSER_PASSWORD=admin \
    --env DJANGO_SUPERUSER_EMAIL=admin@example.com \
    --publish 8100:8100 \
    python:3-alpine \
    scripts/start_django.sh