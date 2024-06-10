import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

app = Celery('dcelery')

app.config_from_object('dcelery.settings', namespace  = 'CELERY') # namespace is CELERY because when you will see setting.py, we are defining all celery related variables with CELERY_

app.autodiscover_tasks()

@app.task
def add_number(a, b):
  return a+b