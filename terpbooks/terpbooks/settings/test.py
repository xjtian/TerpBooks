from __future__ import absolute_import

from .base import *

LOCAL_MEDIA = True

# In-memory test database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

SECRET_KEY = 'super_secret_django_key'

from ..signals import *