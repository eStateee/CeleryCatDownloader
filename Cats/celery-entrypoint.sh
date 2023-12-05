#!/bin/sh

until cd /usr/src/app
do
    echo "Waiting for server volume..."
done

celery -A Cats worker -l info
