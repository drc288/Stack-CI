#!/bin/bash
# This script configure global ENV for the project STACK-CI
STACK_MYSQL_USER=stack_dev \
STACK_MYSQL_PWD=stack_dev_pwd \
STACK_MYSQL_HOST=localhost \
STACK_MYSQL_DB=stack_dev_db \
STACK_TYPE_STORAGE=db \
STACK_ENV=test \
./console.py
