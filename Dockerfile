# Utilisation de l'image Python officielle comme image de base
FROM python:3.10

# Créer un répertoire pour l'application
RUN mkdir /app

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app

# Installer les dépendances Python
RUN rm -rf /root/.cache/pip

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Copier l'application Python dans le conteneur
COPY . /app

# Exposer le port 8000
EXPOSE 8000

# Commande pour exécuter l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
