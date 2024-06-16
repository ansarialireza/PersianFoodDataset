
from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sutsg(e3xrin8bjz7par8)(zsmqs+x$ts^0f0t$u_5mm5eoz0%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'website',
    'accounts',
    'dataset',
    'django_recaptcha',
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

ROOT_URLCONF = 'core.urls'

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


WSGI_APPLICATION = 'core.wsgi.application'


# Database

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE':config('DB_ENGINE', default='django.db.backends.postgresql'),
            'NAME':config('DB_NAME', default='postgres'),
            'USER':config('DB_USER', default='postgres'),
            'PASSWORD':config('PASSWORD', default='1'),
            'HOST':config('HOST', default='127.0.0.1'),
            'PORT':config('PORT', default='5432')
        }
}


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

CKEDITOR_UPLOAD_PATH='uploads/'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# Https settings
if config("USE_SSL_SETTINGS",default=False,cast=bool):
    SECURE_BROWSER_XSS_FILTER = True
    CSRF_COOKIE_SECURE =True
    X_FRAME_OPTIONS = 'SAMEORIGIN'
    SECURE_CONTENT_TYPE_NOSNIFF = True

    ## Strict-Transport-Security
    SECURE_HSTS_SECONDS = 15768000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    ## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
    SECURE_SSL_REDIRECT = True 

    # for more security
    CSRF_COOKIE_SECURE = True
    CSRF_USE_SESSIONS = True
    CSRF_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'Strict'
    
    
RECAPTCHA_PUBLIC_KEY = '6LchX_opAAAAANTgsamqA5K1Ig7IcmIG8lTytHYh'
RECAPTCHA_PRIVATE_KEY = '6LchX_opAAAAAATSr5-VRLsn76h4k4EiArbgaYrN'
# RECAPTCHA_REQUIRED_SCORE = 0.85
SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']
