#!/bin/sh

gunicorn Cats.wsgi:application --bind 0.0.0.0:8000
exec "$@"
