from celery import Celery
import configuration

app1 = Celery('tasks')
print("going to Load configuration into celery")
# app.config_from_object('configuration', namespace  = 'CELERY')
app1.config_from_object('configuration')
# app1.config_from_object('configuration')

print("...............................",app1.conf)