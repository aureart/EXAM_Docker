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

# Installer les paquets requis
#RUN pip3 install requests

# Copier le script de test dans l'image
ADD authentification_test.py /authentification_test.py

# Définir le répertoire de travail
#WORKDIR /app

# Commande à exécuter au démarrage du conteneur
CMD python3 authentification_test.py