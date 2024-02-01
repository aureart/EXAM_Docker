# Dockerfile pour le test d'authorization
FROM ubuntu:18.04

RUN apt-get update && apt-get install python3-pip -y && pip3 install requests

ADD content_test.py /content_test.py
#WORKDIR /app
#EXPOSE 8000
CMD python3 /content_test.py