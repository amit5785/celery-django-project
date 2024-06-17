from celery import shared_task

@shared_task(bind =True)
def addTwoNumbers(self, nums:list):
  print(f'called :: {self.request.task}')
  return sum(nums)