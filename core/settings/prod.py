from .base import *
from urllib.parse import urlparse

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1","127.0.0.1:8000","localhost","localhost:8000","0.0.0.0","0.0.0.0:8000"]


url = urlparse(os.environ.get("DATABASE_URL"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres123",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
    }
}
CELERY_BROKER_URL = "redis://redis:6379/1"

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv("REDIS_URL"),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}