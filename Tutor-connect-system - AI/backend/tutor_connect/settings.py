import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [

'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',

# third party
'rest_framework',
'corsheaders',
'channels',
'daphne',

# local apps
'users',
'tutoring',
'messaging',
'payments',

]

MIDDLEWARE = [

'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'corsheaders.middleware.CorsMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'tutor_connect.urls'

CORS_ALLOW_ALL_ORIGINS = True

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

WSGI_APPLICATION = 'tutor_connect.wsgi.application'

ASGI_APPLICATION = 'tutor_connect.asgi.application'


DATABASES = {

'default':{

'ENGINE':'django.db.backends.postgresql',

'NAME': os.getenv("DB_NAME"),

'USER': os.getenv("DB_USER"),

'PASSWORD': os.getenv("DB_PASSWORD"),

'HOST': os.getenv("DB_HOST"),

'PORT': os.getenv("DB_PORT"),

}

}


AUTH_PASSWORD_VALIDATORS = [

{'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
{'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},
{'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},
{'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'},

]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {

'DEFAULT_AUTHENTICATION_CLASSES': (

'rest_framework_simplejwt.authentication.JWTAuthentication',

)

}


SIMPLE_JWT = {

'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),

'REFRESH_TOKEN_LIFETIME': timedelta(days=1),

}


STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY")