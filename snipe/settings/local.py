"""
DJANGO_SETTINGS_MODULE for local development
"""

from .base_settings import *  # pylint: disable=W0614,W0401
from .conf import *  # pylint: disable=W0614,W0401

DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST_NAME,
        'PORT': DB_PORT,
        'OPTIONS': DB_OPTIONS,
    }
}

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

AZURE_SEARCH_OPTIONS = AZURE_SEARCH_OPTIONS
