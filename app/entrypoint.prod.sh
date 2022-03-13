#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

set -e

echo "${0}: running migrations."
python manage.py makemigrations --merge
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
