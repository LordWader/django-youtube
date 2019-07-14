import os
import celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartpolis.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = celery.Celery('smartpolis')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-request-every-single-minute': {
        'task': 'testapi.tasks.search_func',
        'schedule': crontab(minute='*/1'),
    },
}