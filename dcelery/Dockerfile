FROM python:3.11

#prevent python from writting .pyc files
ENV PYTHONDONTWRITEBYTECODE  1
#ensured that python output is directly sent to terminal without buffering it
ENV PYTHONUNBUFFERED 1
# COPY ./requirements.txt /usr/src/app/
# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# CMD ["ls"]
# RUN chmod -R +rwx ./entrypoint.sh
RUN echo ls -l
CMD [ "/app/entrypoint.sh" ]
# CMD ["ls"]
# CMD ["python", "./manage.py", "runserver", "0.0.0.0:5785"]