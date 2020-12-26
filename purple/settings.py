"""
Django settings for purple project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True),
    ALLOWED_HOSTS=(str, '*'),
    SECRET_KEY=(str, '-pt+1)!d$hca8_esv8)^!0pfqh%&cofmy@1o@bou0zffgrsxio'),
    CORS_ORIGIN_ALLOW_ALL=(bool, True),
    ROOT_URLCONF=(str, 'purple.urls'),
    WSGI_APPLICATION=(str, 'purple.wsgi.application'),
    LANGUAGE_CODE=(str, 'en-us'),
    TIME_ZONE=(str, 'UTC'),
    USE_I18N=(bool, True),
    USE_L10N=(bool, True),
    USE_TZ=(bool, True),
    STATIC_URL=(str, '/static/'),
    STATIC_ROOT=(str, 'static/'),
    # MEDIA_URL=(str, '/media/'),
    # MEDIA_ROOT=(str, 'http://purplecakeboutique.az/'),
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-pt+1)!d$hca8_esv8)^!0pfqh%&cofmy@1o@bou0zffgrsxio'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = [env("ALLOWED_HOSTS")]

CORS_ORIGIN_ALLOW_ALL = env("CORS_ORIGIN_ALLOW_ALL")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = env("ROOT_URLCONF")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = env("WSGI_APPLICATION")

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
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

LANGUAGE_CODE = env("LANGUAGE_CODE")

TIME_ZONE = env("TIME_ZONE")

USE_I18N = env("USE_I18N")

USE_L10N = env("USE_L10N")

USE_TZ = env("USE_TZ")

# STATIC_URL = env("STATIC_URL")
# STATIC_ROOT = env("STATIC_ROOT")

# STATICFILES_DIR = '/root/purple-backend/static'
# STATIC_ROOT = '/root/purple-backend/static'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
STATIC_URL = '/static/'
# STATIC_ROOT = "/var/api.purplecakeboutique.az/static/"
STATIC_ROOT = "static/"

MEDIA_URL = '/media/'
# MEDIA_ROOT = '/root/frontend/public/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT = 'http://purplecakeboutique.az'
# MEDIA_URL = env("MEDIA_URL")
# MEDIA_ROOT = env("MEDIA_ROOT")
# /root/purple-backend/static
# /var/api.purplecakeboutique.az/static/