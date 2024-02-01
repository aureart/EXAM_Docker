# Dockerfile pour le test d'authentification
#FROM python:3.9
#RUN pip install --upgrade pip
#RUN apt-get update
#RUN apt-get install -y python3-pip
#RUN pip3 install requests 
#COPY authentification_test.py /authentification_test.py
#WORKDIR /app
#EXPOSE 8000
#CMD python3 /authentification_test.py
# Dockerfile pour le test d'authentification
FROM python:3.9

RUN apt-get update && apt-get install python3-pip -y && pip install requests

ADD authentification_test.py /authentification_test.py

WORKDIR /app

CMD python3 authentification_test.py