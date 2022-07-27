#! /bin/bash

python3 manage.py makemigrations google_sheets

python3 manage.py migrate --no-input

python3 manage.py collectstatic --no-input

gunicorn kanal_servis.wsgi:application --bind 0.0.0.0:8000