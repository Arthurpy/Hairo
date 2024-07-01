from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

CORS_ALLOW_ALL_ORIGINS = True

SECRET_KEY = 'django-insecure-4ip@6fwhvtkypke2c+1hc7^t@j5r($3^xz)@4(xt%_x%0qhahb'

DEBUG = True

ALLOWED_HOSTS = [
    'https://hairo-back.herokuapp.com',
    'localhost',
]


INSTALLED_APPS = [
    'corsheaders',
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Hairo_Back',
    'rest_framework',
    'rest_framework_simplejwt',
    'webpack_loader',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'Hairo_Back.middleware.JWTAuthenticationMiddleware',
]

SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = True
CSP_DEFAULT_SRC = "'self' data: https:; default-src 'self' http://localhost:8000"

ROOT_URLCONF = 'Hairo_Back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Hairo_Back.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'https://hairo-back.herokuapp.com',
    'http://localhost:8000',
    'http://localhost:5173',
]

CORS_ALLOW_CREDENTIALS = True

APPEND_SLASH = False

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}


STATIC_ROOT =STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

AUTH_USER_MODEL = 'Hairo_Back.User'


AUTHENTICATION_BACKENDS = [
    'Hairo_Back.backends.EmailBackend'
    ]

SOCIALACCOUNT_PROVIDERS = {
}

SITE_ID = 1


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'fichiers_cours')

# settings.py

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
SECRET_KEY = 'your_secret_key'
