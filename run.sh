#! /bin/bash

python manage.py migrate
python manage.py collectstatic --no-input
DJANGO_SUPERUSER_PASSWORD=somethingsupersecret123 python manage.py createsuperuser --username admin --no-input --email admin@admin.noadmin
python manage.py runserver 0.0.0.0:8000
