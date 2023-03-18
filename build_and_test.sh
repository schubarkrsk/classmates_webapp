#!/bin/bash
python3 src\manage.py makemigrations
python3 src\manage.py migrate
python3 src\manage.py runserver