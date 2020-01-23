#!/bin/sh
if [ -n "$DB_HOST" ]; then
    echo "Waiting for database to start..."

    while ! nc -z "$DB_HOST" "$DB_PORT"; do
      sleep 0.1
    done

    echo "Database started"
fi

if [ -n "$SEARCH_HOST" ]; then
    echo "Waiting for Search Engine to start..."

    while ! nc -z "$SEARCH_HOST" "$SEARCH_PORT"; do
      sleep 0.1
    done

    echo "Search Started"
fi


echo "Starting Application"
flask db upgrade
exec flask run -h 0.0.0.0