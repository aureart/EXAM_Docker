# Dockerfile pour le test d'authorization
FROM python:3.8
RUN apt-get update && apt-get install python3-pip -y && pip install requests
COPY authorization_test.py /authorization_test.py
WORKDIR /app
EXPOSE 8000
CMD python3 /authorization_test.py