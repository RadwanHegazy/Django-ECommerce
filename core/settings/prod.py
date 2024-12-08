from .base import *

DEBUG = False
ALLOWED_HOSTS = ["YOUR_DOMAIN"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),       
        'USER': os.getenv("DB_USER"),           
        'PASSWORD': os.getenv("DB_PASSWORD"),   
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../db.sqlite3',
    }
}

