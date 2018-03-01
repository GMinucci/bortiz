#!/bin/bash
set -e
cmd="$@"

export DATABASE_URL=$DATABASE_PREFIX://$POSTGRES_USER:$POSTGRES_PASSWORD@postgres:5432/$POSTGRES_DB

function postgres_ready(){
python << END
import os
import sys
import psycopg2

DATABASE_URL = os.environ.get('DATABASE_URL')

try:
    conn = psycopg2.connect(DATABASE_URL)
except psycopg2.OperationalError:
    sys.exit(-1)

sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - waiting"
  sleep 1
done

exec $cmd
