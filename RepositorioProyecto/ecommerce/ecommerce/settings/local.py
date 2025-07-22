from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-c%w@t00b$f*-8%w26p*lb$zg6i0=5dvpphkr_n$^&$3@tpf3bv'

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

