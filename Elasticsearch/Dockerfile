# Utiliser une image de base Python
FROM python:3.12.5

# Définir le répertoire de travail
RUN mkdir /home/elastic_docker
WORKDIR /home/elastic_docker

# Copier les fichiers nécessaires
COPY . .
COPY requirements.txt  /home/elastic_docker/requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r /home/elastic_docker/requirements.txt
RUN apt-get update && apt-get install -y curl


WORKDIR /home/elastic_docker/DB_ellasticsearch

# Healthcheck pour s'assurer qu'Elasticsearch répond
HEALTHCHECK --interval=30s --timeout=10s --retries=5 \
CMD curl -f http://localhost:9200/ || exit 1

# Commande pour lancer l'application
CMD ["python", "stockage.py"]
