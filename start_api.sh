#!/bin/bash

#export LC_ALL=C.UTF-8
#export LANG=C.UTF-8

# wait for three seconds
echo "<<<<<<<<<<<<<<<<<<<< START API >>>>>>>>>>>>>>>>>>>>>>>>"
sleep 3

# Start the API
gunicorn --workers 3 -t 800000000 app.app:app -b 0.0.0.0:8000 --access-logfile '-'
