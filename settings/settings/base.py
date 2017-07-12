import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if str(config('DEBUG')) == 'True':
    DEBUG = True
    ALLOWED_HOSTS = ['*']
else:
    DEBUG = False
    ALLOWED_HOSTS = ['www.dev2tech.xyz','dev2tech.xyz','174.138.116.15']

SECRET_KEY = config('SECRET_KEY')
ROOT_URLCONF = 'settings.urls'

SITE_ID = 1

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

LOCAL_APPS = [
    'local_apps.api',
    'local_apps.authentication',
    'local_apps.clients',
    'local_apps.frontend',
    'local_apps.medias',
    'local_apps.payments',
    'local_apps.projects',
    'local_apps.services',
    'local_apps.widgets',
]
THIRD_PARTY_APPS = [
    'rest_framework',
    'ckeditor',
]
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settings.settings.custom_context_processors.menu',
                'settings.settings.custom_context_processors.sessions',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'es-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'media'))
STATIC_URL = '/static/'

if str(config('STATIC')) == "Stagging":
    STATIC_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'staticfiles'))
else:
    STATICFILES_DIRS = (
        os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'staticfiles')),
    )

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_SSL = config('EMAIL_USE_SSL')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
LOGIN_URL = 'dashboard'
LOGIN_REDIRECT_URL = '/dashboard/'
SITE_URL = 'http://www.dev2tech.xyz'
LOGOUT_REDIRECT_URL = SITE_URL
SESSION_COOKIE_AGE = 43200
SESSION_COOKIE_NAME = 'session'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'local_apps.authentication.EmailBackend.EmailBackend',
]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True