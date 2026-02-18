#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create superuser if needed (optional)
# python manage.py createsuperuser --noinput

exec "$@"
