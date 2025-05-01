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
- `.github/workflows/ci.yml` :  Microservices local deployment
## CI/CD

Jede Änderung in `main` löst Tests und Linter aus.

# Edu App with Traefik

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
```bash
docker-compose run web python manage.py collectstatic
(test)
http://localhost/static/admin/css/base.css

## wenn added logo.png 
docker-compose up # logo display ==Du kannst es in deiner Django-App mit WhiteNoise oder über den Traefik-Proxy ausliefern.
(test)
http://localhost/edu/ → Django Views
http://localhost/edu/static/css/main.css → direkt aus staticfiles/ via WhiteNoise

## und dann
```python
pip install whitenoise
python manage.py collectstatic
