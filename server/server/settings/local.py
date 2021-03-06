from .base import *

DEBUG = True

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecomstore',
        'USER': 'sharmi',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': ''
    }
}

# Memcached

CACHE_BACKEND = 'memcached://127.0.0.1:11211'
