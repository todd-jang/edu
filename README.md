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
