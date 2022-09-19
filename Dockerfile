FROM python:3.7

WORKDIR /fastapi-app

#ARG var1
#ARG var2

#ENV env1=${var1}
#ENV env2=${var2}

#RUN echo ${env1}
#Run echo ${env2}

COPY requirements.txt .

RUN wget -c https://github.com/dusan-madzarevic/post-microservice/releases/latest/download/dislinkt-post-1.0.tar.gz -O - | tar -xz

#RUN pip install -r requirements.txt

COPY ./app ./app

ENV PYTHONPATH "${PYTHONPATH}:/app"

#CMD $env1 $env2
CMD ["python", "./app/main.py"]

#docker build -t imeslike --build-arg var1=python --build-arg var2=./app/main.py .
#docker run -p 8003:8003  imeslike 

#ili

#docker build -t post_test --build-arg var1=python --build-arg var2=./app/integration_test.py .
#docker run post_test