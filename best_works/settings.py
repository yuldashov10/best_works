from pathlib import Path

from decouple import Csv, config
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("SECRET_KEY", default=get_random_secret_key(), cast=str)
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

INSTALLED_APPS = [
    "jet.dashboard",
    "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    #
]

INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "best_works.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "best_works.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", cast=str),
        "NAME": config("DB_NAME", cast=str),
        "USER": config("DB_USER", cast=str),
        "PASSWORD": config("DB_PASSWORD", cast=str),
        "HOST": config("DB_HOST", cast=str),
        "PORT": config("DB_PORT", cast=int),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru-Ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / "static/"]
else:
    STATIC_ROOT = BASE_DIR / "static/"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
