from pathlib import Path
import os

from dotenv import load_dotenv
from celery.schedules import crontab

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(", ")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.parser',
    'django_celery_beat',
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

ROOT_URLCONF = 'finnhub_parser.urls'

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

WSGI_APPLICATION = 'finnhub_parser.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DB_ENGINE"),
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT")
    }
}

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

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_TZ = False
USE_L10N = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery settings
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")

# There are 5 schedules, that will be executed each hour
# Each schedule is for each ticker
# For each schedule will be responsible only one task, but with different ticker argument
CELERY_BEAT_SCHEDULE = {
    "parsing_tsla": {
        "task": "apps.parser.tasks.parsing_news",
        "schedule": crontab(hour="*", minute=0),
        "args": (("TSLA"),)
    },
    "parsing_amzn": {
        "task": "apps.parser.tasks.parsing_news",
        "schedule": crontab(hour="*", minute=0),
        "args": (("AMZN"),)
    },
    "parsing_meta": {
        "task": "apps.parser.tasks.parsing_news",
        "schedule": crontab(hour="*", minute=0),
        "args": (("META"),)
    },
    "parsing_msft": {
        "task": "apps.parser.tasks.parsing_news",
        "schedule": crontab(hour="*", minute=0),
        "args": (("MSFT"),)
    },
    "parsing_nflx": {
        "task": "apps.parser.tasks.parsing_news",
        "schedule": crontab(hour="*", minute=0),
        "args": (("NFLX"),)
    }
}

TICKERS = os.environ.get("TICKERS").split(",")

SUPERUSER_USERNAME = os.environ.get("SUPERUSER_USERNAME")
SUPERUSER_MAIL = os.environ.get("SUPERUSER_MAIL")
SUPERUSER_PASSWORD = os.environ.get("SUPERUSER_PASSWORD")

FINNHUB_TOKEN = os.environ.get("FINNHUB_TOKEN")