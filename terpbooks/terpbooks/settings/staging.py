from __future__ import absolute_import

from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'super_secret_django_key'
USE_CAS = True

if USE_CAS:
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'cas.backends.CASBackend',
    )

    MIDDLEWARE_CLASSES += (
        'cas.middleware.CASMiddleware',
    )
