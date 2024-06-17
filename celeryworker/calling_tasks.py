# from celeryworker.celery import celery_app as celeryInst

# celeryInst.send_task('celeryworker.custom_tasks.addition_tasks.addTwoNumbers', args = tuple([[1,2,3,5]]))

import sys
import os

# Add the project directory to the PYTHONPATH
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from celeryworker.celery_configs import celery_app as celeryInst
from celery_configs import app as celeryInst

# Now try sending the task
celeryInst.send_task('custom_tasks.addition_tasks.addTwoNumbers', args=tuple([[1, 2, 3, 5]]))