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
    --publish 8100:8100 \
    python:3-alpine \
    scripts/start_django.sh