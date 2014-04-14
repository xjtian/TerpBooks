from __future__ import absolute_import

import os

from django.core.exceptions import ImproperlyConfigured

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG


def get_env_variable(var_name):
    """ Get the environment variable with specified name or throw exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the %s environment variable.' % var_name
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('DJANGO_SECRET')

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


def custom_show_toolbar(self):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'terpbooks.settings.local.custom_show_toolbar',
}