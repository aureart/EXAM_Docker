# Dockerfile pour le test d'authentification
FROM python:3.8
RUN pip install --upgrade pip
RUN pip install requests 
COPY authentification_test.py /authentification_test.py
WORKDIR /app
EXPOSE 8000
CMD python3 /authentification_test.py
