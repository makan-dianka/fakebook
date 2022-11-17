"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from django.core.management.utils import get_random_secret_key
from pathlib import Path
import os
import random

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# generate secret key 
path = os.path.join(BASE_DIR, 'secret_keys')
if os.path.exists(path):
    pass
else:
    with open(path, 'w') as keys:
        for i in range(1, 11):
            keys.write(f"{get_random_secret_key()}\n")


# SECURITY WARNING: keep the secret key used in production secret!
with open(path, 'r') as secret_keys:
    SECRET_KEY = random.choice(secret_keys.readlines())


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

dev_hosts = os.environ.get("DEV_HOST").split(';')
if DEBUG:
    if len(dev_hosts) != 0:
        ALLOWED_HOSTS = [host for host in dev_hosts]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'web.wsgi.application'

 
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('NAME'),
        'HOST' : os.environ.get('HOST'),
        'USER' : os.environ.get('USER'),
        'PASSWORD' : os.environ.get('PASSWORD'),
        'PORT' : os.environ.get('PORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# email conf 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


# logger
if DEBUG==True:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,

        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(lineno)s %(message)s',
            },

            'simple': {
                'format': '%(levelname)s %(message)s',
            },
        },

        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },

        'handlers': {
            'errors': {
                'filename' :  os.path.join(BASE_DIR, 'logs/errors.log'),
                'filters': ['require_debug_true'],
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'verbose',
                'backupCount' : 5,
                'maxBytes' : 1024*1024*50,
                'encoding' : 'utf8',
                'level': 'DEBUG',
            },

        },

        'loggers': {
            'errors_log': {
                'handlers': ['errors'],
                'level': 'DEBUG',
                'level': 'INFO',
            },
        }
    }