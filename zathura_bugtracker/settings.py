"""
Django settings for zathura_bugtracker project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from decouple import config
from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Never Go Live with Debug - True!

# Using of wildcard is really dangerous
ALLOWED_HOSTS = ['bugtracker.shepherd06.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ping_app.apps.PingAppConfig',
    'frontend.apps.FrontendConfig',
    'error_logger.apps.ErrorLoggerConfig',
    'token_manager.apps.TokenManagerConfig',
    'user.apps.UserConfig',
    'projects.apps.ProjectsConfig',
    'team.apps.TeamConfig',
    'organization.apps.OrganizationConfig',
    'rest_framework',
    'guardian',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_referrer_policy.middleware.ReferrerPolicyMiddleware',
]

ROOT_URLCONF = 'zathura_bugtracker.urls'

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
    # {
    #     'BACKEND': 'django.template.backends.jinja2.Jinja2',
    #     'DIRS': [
    #         os.path.join(BASE_DIR, 'templates'),
    #     ],
    #     'APP_DIRS': True,
    # },
]

WSGI_APPLICATION = 'zathura_bugtracker.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("DB_NAME", None),
        'USER': config("DB_USER", None),
        'PASSWORD': config("DB_PASSWORD", None),
        'HOST': config("DB_URL", None),
        'PORT': config("DB_PORT", None),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS512',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_bugtracker")

"""
APPEND_SLASH

Default: True

When set to True, if the request URL does not match any of the patterns in the URLconf 
and it doesn’t end in a slash, an HTTP redirect is issued to the same URL with a 
slash appended. Note that the redirect may cause any data submitted in a POST
request to be lost.
"""

APPEND_SLASH = True

AUTH_USER_MODEL = 'user.CustomUser'  # new

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)

# SECURE_BROWSER_XSS_FILTER = True   # Protection against X-XSS
SECURE_CONTENT_TYPE_NOSNIFF = True   # X-Content-Type-Options
X_FRAME_OPTIONS = 'DENY'  # X-Frame-Options
REFERRER_POLICY = 'same-origin'  # Referrer-Policy
