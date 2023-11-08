# Utilisation de l'image Python officielle comme image de base
FROM python:3.8

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Définir le répertoire de travail
WORKDIR /app

# Copier l'application Python dans le conteneur
COPY . .

# Exposer le port 8000
EXPOSE 8000

# Commande pour exécuter l'application Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

