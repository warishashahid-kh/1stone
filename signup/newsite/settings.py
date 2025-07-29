# signup/newsite/settings.py

import os # Standard Django import, often used for path manipulation.
from pathlib import Path # Standard Django import, modern way for path manipulation.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent # Standard Django definition. This calculates the path to your 'signup' root directory.

# SECURITY WARNING: keep the secret key used in production secret!
# IMPORTANT: In a real production environment, replace 'django-insecure-your-secret-key-here'

SECRET_KEY = 'django123456788warishablah blah'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allowed hosts for your Django application.
# In development, you can leave it empty or add '127.0.0.1', 'localhost'.
# In production, you MUST list your domain names (e.g., ['www.example.com']).
ALLOWED_HOSTS = []


# Application definition - lists all Django apps enabled for this project.
INSTALLED_APPS = [
    'django.contrib.admin', # Standard Django app for the admin interface.
    'django.contrib.auth', # Standard Django app for authentication and permissions.
    'django.contrib.contenttypes', # Standard Django app for content types system.
    'django.contrib.sessions', # Standard Django app for session management.
    'django.contrib.messages', # Standard Django app for displaying one-time messages.
    'django.contrib.staticfiles',
    'loginapp',

]

# Middleware classes that process requests and responses.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Standard Django for security features.
    'django.contrib.sessions.middleware.SessionMiddleware', # Standard Django for session handling.
      'django.middleware.common.CommonMiddleware', # Standard Django for common utilities (e.g., handling trailing slashes).
    'django.middleware.csrf.CsrfViewMiddleware', # Standard Django for CSRF protection.
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Standard Django for user authentication.
    'django.contrib.messages.middleware.MessageMiddleware', # Standard Django for message handling.
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Standard Django for preventing clickjacking attacks.
]

# The main URL configuration for your project.
ROOT_URLCONF = 'newsite.urls'  # Standard Django. This tells Django where your main URL patterns are defined.

# Template engine configuration.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Standard Django. Specifies the template engine.
        'DIRS': [],  # Standard Django. Left empty as we're using app_dirs.
        'APP_DIRS': True,  # Standard Django. Tells Django to look for 'templates' folders inside your INSTALLED_APPS.
        'OPTIONS': {
            'context_processors': [ # Standard Django. These add common variables to templates.
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application for serving your project.
WSGI_APPLICATION = 'newsite.wsgi.application'  # Standard Django. Entry point for web servers.

# Database configuration. SQLite is used by default for development.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Standard Django. Specifies SQLite database.
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation rules.
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


LANGUAGE_CODE = 'en-us' # Standard Django.
TIME_ZONE = 'UTC' # Standard Django.
USE_I18N = True # Standard Django.
USE_TZ = True # Standard Django.


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'