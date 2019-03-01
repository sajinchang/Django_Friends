#!/bin/bash

PROJECT_DIR='/opt/Django_TanTan'

cd $PROJECT_DIR
#source .venv/bin/activate
gunicorn -c Django_TanTan/gunicorn_config.py Django_TanTan.wsgi
#deactivate
