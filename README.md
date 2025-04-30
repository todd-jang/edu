# Django Edu API

Dies ist ein Beispielprojekt für eine Bildungs-API, gebaut mit Django und Docker Compose.

## Schnellstart

```bash
docker-compose up --build
```

API ist erreichbar unter: `http://localhost:8000`

## Struktur

- `app/`: Django Projekt
- `Dockerfile`, `docker-compose.yml`: Containerisierung
- `.github/workflows/django.yml`: CI/CD mit GitHub Actions

## CI/CD

Jede Änderung in `main` löst Tests und Linter aus.

# Edu-Traefik-Example

Ein Beispiel-Django-Projekt, das über Traefik als Reverse Proxy läuft.

## Dienste

- Django API auf Port 8000 → erreichbar via http://localhost
- PostgreSQL Datenbank
- Traefik Dashboard → http://localhost:8080

## Start


```bash
docker-compose up --build
```python
python manage.py runserver

##fuer MVPs and upto mid-size Apps
python -m http.server 8001 --directory ./staticfiles
