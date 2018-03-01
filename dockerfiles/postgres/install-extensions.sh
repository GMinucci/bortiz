#!/bin/bash
set -e

echo "Installing extensions..."
psql -v ON_ERROR_STOP=1 -d $POSTGRES_DB --username "$POSTGRES_USER" <<-EOSQL
EOSQL
echo "Extensions successfully installed!"
