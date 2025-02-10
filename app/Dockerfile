# Utiliser une image de base Python
FROM python:3.12.5

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY . /app
COPY requirements.txt  /app/requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exposer le port 8050 (port par défaut pour Dash)
EXPOSE 8050

# Commande pour lancer l'application
CMD ["python", "/app/main.py"]
