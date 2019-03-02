#!/bin/bash

PROJECT_DIR='/opt/Django_Friends'

cd $PROJECT_DIR
#source .venv/bin/activate
gunicorn -c Django_Friends/gunicorn_config.py Django_Friends.wsgi
#deactivate
