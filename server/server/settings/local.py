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

