from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret_setting('SECRET_KEY')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret_setting('DATABASE_NAME'),
        'USER': get_secret_setting('DATABASE_USER'),
        'PASSWORD': get_secret_setting('DATABASE_PASSWORD'),
        'HOST': get_secret_setting('DATABASE_HOST'),
        'PORT': get_secret_setting('DATABASE_PORT'),
    }
}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
