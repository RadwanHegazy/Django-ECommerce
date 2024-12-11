from __future__ import absolute_import, unicode_literals
import os
from dotenv import load_dotenv
from celery import Celery
from django.conf import settings

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE',f'core.settings.{os.getenv("SERVER_STATE")}')

app = Celery('core')
app.conf.enable_utc = False

app.conf.update(timezone = 'Africa/Cairo')


app.config_from_object(settings, namespace='CELERY')


# CELERY BEAT SETTINGS  

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task (self) : 
    print(f'Request : ', {self.request})