# Dockerfile pour le test d'authorization
FROM ubuntu:18.04

RUN apt-get update && apt-get install python3-pip -y && pip3 install requests

ADD authorization_test.py /authorization_test.py
#WORKDIR /app
#EXPOSE 8000
CMD python3 /authorization_test.py