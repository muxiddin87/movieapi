#!/bin/bash

sleep 10

sudo lsof -i :5432

python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
