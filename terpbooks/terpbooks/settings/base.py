from unipath import Path

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.core.urlresolvers import reverse_lazy

# Paths
PROJECT_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = PROJECT_DIR.child('media')
STATIC_ROOT = PROJECT_DIR.child('static')

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
)

STATICFILES_DIRS = (
    PROJECT_DIR.child('assets'),
)

STATIC_URL = '/static/'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'south',
    'books',
    'transactions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'terpbooks.urls'

WSGI_APPLICATION = 'terpbooks.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'terpbooks',
        'USER': 'root',
        'PASSWORD': '',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'EST'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# CAS config
USE_CAS = False

CAS_SERVER_URL = 'https://login.umd.edu/cas/'
CAS_VERSION = '2'
CAS_LOGOUT_COMPLETELY = True

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

LOGIN_REDIRECT_URL = reverse_lazy('profile')