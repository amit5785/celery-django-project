import os

# CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0')
# CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/0')

broker_url = 'redis://redis:7320/0'
result_backed = 'redis://redis:7320/0'

print("Loading configuration into celery")