FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERD 1

COPY . /app
WORKDIR /app/celeryworker
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["celery", "-A", "celery_configs", "worker", "-l", "INFO"]