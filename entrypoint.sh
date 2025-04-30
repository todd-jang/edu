#!/bin/sh
#option
echo "Running collectstatic..."
python manage.py collectstatic --noinput

exec "$@"
