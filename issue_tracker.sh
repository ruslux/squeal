#!/usr/bin/env bash

cd $(dirname "$0")
while true; do
    for file in *.log ; do
        if [ "$(cat ${file})" ]; then
            kill $(ps aux | awk '/[s]queal/ {print $2}') > /dev/null 2>&1 &
            ISSUE="$(cat *.log)"
            python3 issue_reporter.py "${file}" "${ISSUE}"
            mv "${file}" "${file}.old"
            sh start.sh &
            exit 1
        fi
    done
    sleep 10m
done
