python manage.py migrate --no-input;
celery -A DiplomProject beat -l info
