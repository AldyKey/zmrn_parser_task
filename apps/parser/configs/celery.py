import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finnhub_parser.settings")

app = Celery("parser")
app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks()

