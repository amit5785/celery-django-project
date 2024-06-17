from celery import shared_task

@shared_task(bind = True)
def lengthOfString(self, s: str):
  print(f'Called :: {self.request.task}')
  return len(str)