#!/bin/bash

PROJECT_DIR='/opt/Django_Friends'
PIDFILE="$PROJECT_DIR/logs/gunicorn.pid"

kill `cat $PIDFILE`
