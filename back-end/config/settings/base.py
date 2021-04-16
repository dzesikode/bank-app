"""
Django settings for bankproject project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import environ

env = environ.Env()
env.read_env(env_file='config/.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bankapp',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bankproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bankproject.wsgi.application'

DEFAULT_USERS = {
    'admin': 'ADMIN',
    'product_manager': 'PRODUCT-MANAGER',
    'test_user': 'USER'
}

DEFAULT_PRODUCTS = [
    {
        'name': 'Current Account',
        'age': ['ADULT', 'SENIOR'],
        'student': False,
        'income': ['LOW_INCOME', 'MEDIUM_INCOME', 'HIGH_INCOME'],
    },
    {
        'name': 'Current Account Plus',
        'age': ['ADULT', 'SENIOR'],
        'student': False,
        'income': ['HIGH_INCOME'],
    },
    {
        'name': 'Junior Saver Account',
        'age': ['JUNIOR'],
        'student': False,
        'income': ['NO_INCOME', 'LOW_INCOME', 'MEDIUM_INCOME', 'HIGH_INCOME'],
    },
    {
        'name': 'Student Account',
        'age': ['ADULT', 'SENIOR'],
        'student': True,
        'income': ['NO_INCOME', 'LOW_INCOME', 'MEDIUM_INCOME', 'HIGH_INCOME'],
    },
    {
        'name': 'Debit Card',
        'age': ['ADULT', 'SENIOR'],
        'student': False,
        'income': ['NO_INCOME', 'LOW_INCOME'],
    },
    {
        'name': 'Credit Card',
        'age': ['ADULT', 'SENIOR'],
        'student': False,
        'income': ['MEDIUM_INCOME', 'HIGH_INCOME'],
    },
    {
        'name': 'Gold Credit Card',
        'age': ['ADULT', 'SENIOR'],
        'student': False,
        'income': ['HIGH_INCOME'],
    },
]



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'NON_FIELD_ERRORS_KEY': 'global',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
REST_USE_JWT = True

# CORS Header settings
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
    'http://localhost:8000',
    'http://localhost:4200'
)

# Override default User model with a custom one
AUTH_USER_MODEL = 'bankapp.CustomUser'