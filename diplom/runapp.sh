#!/bin/bash
set -x
python manage.py migrate
python manage.py runserver
