#!/bin/ash

echo "Running database migration"
python manage.py migrate

exec "$@"