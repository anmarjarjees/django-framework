"""
Django settings for abccollege project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# We are importing the os to be used in this settings:
import os

import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# Anmar: We changed the secret key by adding the following code from Django docs:
# SECRET_KEY = ''
# Here is the pattern from Django docs:
# with open('/etc/secret_key.txt') as f:
    # SECRET_KEY = f.read().strip()

# we can change the 'etc

# For Heroku, we need to change the App setting by adding the secret key value:
# Opening App Dashboard ==> settings ==> Config Vars
# It's better to have if condition to check if the file is exist or not:
if os.path.exists("secret_key.txt"):
    with open('abccollege/secret_key.txt') as f:
        SECRET_KEY = f.read().strip()


# SECURITY WARNING: don't run with debug turned on in production!
# True for Development and False for deployment
DEBUG = False

# NOTE: 
# if we make DEBUG = False, we do have to specify at least one HOST as shown below:
# otherwise, you will recieve this error: 
# CommandError: You must set settings.ALLOWED_HOSTS if DEBUG is False.
# Examples: 
# ********
# Heroku: The full url is: 'https://anmar-django-demo.herokuapp.com/'
# ALLOWED_HOSTS = ['anmar-django-demo.herokuapp.com']

# Local Server (PC): The full url is: 'http://127.0.0.1:8000'
# ALLOWED_HOSTS = ['127.0.0.1']

# We can keep it empty for local development
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
]

MIDDLEWARE = [
    # Anmar: Here is the comment and the item we copied from Heroku doc
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Anmar: We need to add this constant "STATICFILES_STORAGE" based on Heroku docs
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'abccollege.urls'

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

WSGI_APPLICATION = 'abccollege.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Anmar: Our code starting below:
# We need to add a setting called: STATICFILES_DIRS (All in uppercase)
# This constant will be equal to a list (array) that contains a list of directories 
# Django will use this List to look at the directories for serving all the static assets
# Heroku will use this constant list to find the static assets
# Extra places for collectstatic to find static files: 
# Read more: https://devcenter.heroku.com/articles/django-assets
# NOTE:
# Notice that we are using the "os" module, so we have to import it into this file at the top
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Notice that Django gave us this list "STATICFILES_DIRS" and we modified it:
STATICFILES_DIRS = [
    # To refer to the static folder at the top level of our project (that we created)
    # we need to add an entry that calls os.path.join()
    # with the argument "BASE_DIR" followed by the string 'static'
    # BASE_DIR this constant is defined by Django at the top of this file (BASE_DIR) 
    # BASE_DIR: refers to the directory where manage.py is created
    # Which is the base directory of our project and that's why it's called BASE_DIR
    os.path.join(BASE_DIR,'static'),
    
    # os.path.join():
    # is a python built-in function that provides a cross platform way to build file paths
]

# Based on Heroku docs:
# We need to add the following to the bottom of settings.py:
# The link: https://devcenter.heroku.com/articles/django-app-configuration#settings-py-changes
# Activate Django-Heroku.
django_heroku.settings(locals())