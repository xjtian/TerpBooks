from __future__ import absolute_import

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'super_secret_django_key'

CORS_ORIGIN_ALLOW_ALL = True

# Don't use CAS in local for now
USE_CAS = False

if USE_CAS:
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'cas.backends.CASBackend',
    )

    MIDDLEWARE_CLASSES += (
        'cas.middleware.CASMiddleware',
    )

INSTALLED_APPS += ('debug_toolbar',)


def custom_show_toolbar(request):
    if request.is_ajax():
        return False

    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'terpbooks.settings.local.custom_show_toolbar',
}

from ..signals import *
