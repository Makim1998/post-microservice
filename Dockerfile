FROM python:3.7

WORKDIR /fastapi-app

COPY requirements.txt .

RUN wget -c https://github.com/dusan-madzarevic/post-microservice/releases/latest/download/dislinkt-post-1.0.tar.gz -O - | tar -xz

COPY ./app ./app

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python", "./app/main.py"]
