"""
Global configuration for the OrderManagementBackend Django project.
Handles settings for development and production environments.
"""

from pathlib import Path
from datetime import timedelta
import os

import dj_database_url
from environ import Env

# Initialize environment variables
env = Env()
Env.read_env()

# Base directory setup
BASE_DIR = Path(__file__).resolve().parent.parent
ENVIRONMENT = env("ENVIRONMENT", default="production")

# Security settings
SECRET_KEY = env("SECRET_KEY")
ENCRYPTED_KEY = env("ENCRYPT_KEY")
DEBUG = ENVIRONMENT == "development"
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "ordermanagement-production-0b45.up.railway.app"]
CSRF_TRUSTED_ORIGINS = [
    "https://ordermanagement-production-0b45.up.railway.app",
    "https://polishlodypartner.vercel.app",
]

# Installed applications
INSTALLED_APPS = [
    # Django core apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "cloudinary_storage",
    "cloudinary",
    "rest_framework",
    "corsheaders",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "admin_honeypot",
    "whitenoise",
    # Project-specific apps
    "products",
    "users",
    "orders",
    "cart",
]

# Middleware configuration
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Moved up for CORS priority
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL and template settings
ROOT_URLCONF = "OrderManagementBackend.urls"
WSGI_APPLICATION = "OrderManagementBackend.wsgi.application"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", default="ordermanagement_test_db"),
        "USER": env("DB_USER", default="ordermanagement_user"),
        "PASSWORD": env("DB_PASSWORD", default="testpass123"),
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
    }
}
USE_POSTGRES_LOCALLY = env.bool("USE_POSTGRES_LOCALLY", default=False)
if ENVIRONMENT == "production" or USE_POSTGRES_LOCALLY:
    DATABASES["default"] = dj_database_url.parse(env("DATABASE_URL"))

# Authentication settings
AUTH_USER_MODEL = "users.CustomUser"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    {"NAME": "users.validators.CustomPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "CET"
USE_I18N = True
USE_TZ = True

# Static and media files
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
if ENVIRONMENT == "production" or USE_POSTGRES_LOCALLY:
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
else:
    MEDIA_ROOT = BASE_DIR / "media"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": env("CLOUD_NAME"),
    "API_KEY": env("CLOUD_API_KEY"),
    "API_SECRET": env("CLOUD_API_SECRET"),
}

# CORS settings
CORS_ALLOWED_ORIGINS = ["http://localhost:5173", "https://polishlodypartner.vercel.app"]
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# REST Framework and JWT settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# API documentation settings
SPECTACULAR_SETTINGS = {
    "TITLE": "Polish Lody API",
    "DESCRIPTION": "API dla aplikacji Polish Lody Partner",
    "VERSION": "1.0.0",
}

# Miscellaneous
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ACCOUNT_USERNAME_BLACKLIST = ["admin", "konto", "profil", "smak", "polishlody", "boss"]
