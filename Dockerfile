FROM python:3.7

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python", "./app/main.py"]