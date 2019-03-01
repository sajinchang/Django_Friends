#!/bin/bash

PROJECT_DIR='/opt/Django_TanTan'
PIDFILE="$PROJECT_DIR/logs/gunicorn.pid"

kill `cat $PIDFILE`
