"""
Django settings for registration_manager project.
"""

import environ


from django.utils.translation import gettext_lazy as _
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

root = environ.Path(__file__) - 2  # get root of the project
env = environ.Env()
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('REGISTRATION_MANAGER_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('REGISTRATION_MANAGER_DEBUG', default=False)

ALLOWED_HOSTS = env.list('REGISTRATION_MANAGER_ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'active_link',
    'tempus_dominus',
    'crispy_forms',
    'django_filters',
    'environ',
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

ROOT_URLCONF = 'registration_manager.urls'

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

WSGI_APPLICATION = 'registration_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': env.db('REGISTRATION_MANAGER_DATABASE_URL')
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-gb'

LANGUAGES = [
    ('en', _('English'))
]

DATE_INPUT_FORMAT = [
    '%d &B %Y',
]

DATETIME_INPUT_FORMAT = [
    '%Y/%m/%s %H:%M'
]

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = env.path('REGISTRATION_MANAGER_STATIC_ROOT')
STATIC_URL = '/static/'

# E-mail configuration

EMAIL_CONFIG = env.email_url(
    'REGISTRATION_MANAGER_EMAIL',
    default='consolemail://'
)

# Further configuration
# Project settings
LOGIN_URL = env.str('REGISTRATION_MANAGER_LOGIN_URL', default='login')

# Tempus dominus
TEMPUS_DOMINUS_LOCALIZE = True

# Crispy forms
CRISPY_TEMPLATE_PACK = env.str(
    'REGISTRATION_MANAGER_CRISPY_TEMPLATE_PACK',
    default='bootstrap4'
)


MEDIA_URL = '/media/'
MEDIA_ROOT = env.path('REGISTRATION_MANAGER_MEDIA_ROOT')
