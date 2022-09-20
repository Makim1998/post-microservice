FROM python:3.7

WORKDIR /fastapi-app

COPY requirements.txt .


RUN curl https://github.com/dusan-madzarevic/post-microservice/releases/latest/download/dislinkt-post-1.0.tar.gz \
  | tar -xjC /tmp/dislinkt-post-1.0 \
  && make -C /tmp/dislinkt-post-1.0

COPY ./tmp/dislinkt-post-1.0/app ./app

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python", "./app/main.py"]
