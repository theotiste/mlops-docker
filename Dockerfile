FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exposer le port utilisé par Flask
EXPOSE 5000

# Utiliser gunicorn comme serveur de production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
