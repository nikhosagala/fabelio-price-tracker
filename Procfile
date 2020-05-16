web: gunicorn fabelio_price_tracker.app.wsgi --log-file -
celery: celery -A fabelio_price_tracker.app worker -l info --beat
