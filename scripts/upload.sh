#!/bin/bash

LOCAL_DIR='./'
REMOTE_DIR='/opt/Django_Friends'

USER='root'
HOST='samsa.xin'

rsync -crvP --exclude={.git*,.venv,logs,__pycache__,.idea,medias,db.sqlite3,.qiniu_*} $LOCAL_DIR $USER@$HOST:$REMOTE_DIR/

# 远程重启
ssh $USER@$HOST "$REMOTE_DIR/scripts/restart.sh"
