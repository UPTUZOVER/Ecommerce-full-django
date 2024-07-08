import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
from .django_uziniki import middleware, auth_password_validators, tamplates
from .database import  databases
from .install_app import installed_apps, parler_languages, rest_framework, simple_jwt, jazzmin_settings


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "Account.User"

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = installed_apps

PARLER_LANGUAGES = parler_languages

REST_FRAMEWORK = rest_framework

SIMPLE_JWT = simple_jwt

JAZZMIN_SETTINGS = jazzmin_settings

MIDDLEWARE = middleware

ROOT_URLCONF = "core.urls"

TEMPLATES = tamplates

WSGI_APPLICATION = "core.wsgi.application"

CORS_ALLOW_ALL_ORIGINS = True
DJOSER = {'SERIALIZERS':{"user_create":"user_base.serializers.MyUserSerializer"}}


DATABASES = databases

AUTH_PASSWORD_VALIDATORS = auth_password_validators

LANGUAGE_CODE = "en-us"



TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True



STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'











