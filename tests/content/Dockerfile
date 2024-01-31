# Dockerfile pour le test d'authorization
FROM python:3.9
#RUN pip install --upgrade pip
RUN pip3 install requests
ADD content_test.py /content_test.py
WORKDIR /app
EXPOSE 8000
CMD python3 /content_test.py