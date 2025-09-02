from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Optional: für zusätzliche Komprimierung & Caching
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'edu_api/static'),
]
SECRET_KEY = 'dein-geheimer-schlüssel'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "storages",
    # Weitere Apps
]

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = "minioadmin"
AWS_SECRET_ACCESS_KEY = "minioadmin"
AWS_STORAGE_BUCKET_NAME = "media"
AWS_S3_ENDPOINT_URL = "http://minio:9000"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ⬅️ hier
    
    # Weitere Middleware
]

ROOT_URLCONF = 'edu_api.urls'

WSGI_APPLICATION = 'edu_api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
