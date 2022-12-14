#!/bin/bash
set -e

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

uwsgi --http 0.0.0.0:8000 --master --enable-threads --module web.wsgi
uwsgi --ini web_uwsgi.ini