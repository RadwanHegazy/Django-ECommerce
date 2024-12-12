from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ["localhost","localhost:8000"]


DATABASES = {
    'default': dj_database_url.parse(os.getenv("MYSQL_DB_URL"))
}


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv("REDIS_URL"),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}