"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from .settings.base import load_settings

from django.core.wsgi import get_wsgi_application

load_settings()
application = get_wsgi_application()
