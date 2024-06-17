from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryworker.configuration')


# app.autodiscover_tasks(['celeryworker.custom_tasks'])

@app.task(bind = True)
def fun(self):
  print(f"Called :: {self.request.task}")