from celery import shared_task

@shared_task(bind = True)
def add(self, a, b):
  print(f"Called ::: {self.request.task}")
  return a+b