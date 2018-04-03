#!/usr/bin/env bash

export PYTHONPATH="$(pwd)"/validate_it:$PYTHONPATH
py.test tests --cov=squeal_bot
