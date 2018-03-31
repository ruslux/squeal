#!/bin/bash

kill $(ps aux | awk '/[s]queal/ {print $2}') > /dev/null 2>&1 &

cd $(dirname "$0")
BASEDIR=$(pwd)
mkdir -p data/db
mongod --dbpath "${BASEDIR}/data/db" > /dev/null 2>mongodb.log &
python3 "${BASEDIR}/src" > /dev/null 2>python.log &
sh "${BASEDIR}/issue_tracker.sh" > /dev/null 2>&1 &
