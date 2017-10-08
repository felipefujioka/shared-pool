#!/usr/bin/env bash

eval $(cat app/res/secrets/envfile)

export PGPASSWORD=$DB_PASSWORD

psql --host $DB_HOST --port $DB_PORT --user $DB_USER $DB_NAME