# Utiliser une image de base Python
FROM python:3.12.5

# Définir le répertoire de travail
RUN mkdir /home/Mongo_docker
WORKDIR /home/Mongo_docker

# Copier les fichiers nécessaires
COPY . .
COPY requirements.txt  /home/Mongo_docker/requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r /home/Mongo_docker/requirements.txt

WORKDIR  /home/Mongo_docker


# Commande pour lancer l'application
CMD ["python", "stock_in_mongo.py"]
