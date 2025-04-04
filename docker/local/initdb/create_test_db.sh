#!/bin/sh
set -e

DB_NAME="${POSTGRES_DB}_test"

echo "Creation database test: $DB_NAME"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
  CREATE DATABASE $DB_NAME WITH OWNER = $POSTGRES_USER;
EOSQL

echo "databases '$DB_NAME' created successfully."