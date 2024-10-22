import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(__file__) #afiseaza calea catre fisierul curent
print(BASE_DIR) #afiseaza calea catre directorul parinte al directorului curent
TEMPLATE_DIR=os.path.join(BASE_DIR,"templates") #TEMPLATE_DIR este calea catre directorul templates din proiectul nostru 
STATIC_DIR=os.path.join(BASE_DIR,"static") #STATIC_DIR este calea catre directorul static din proiectul nostr
MEDIA_DIR=os.path.join(BASE_DIR,"media") #MEDIA_DIR este calea catre directorul media din proiectul nostru
SECRET_KEY = 'django-insecure-^1o!i^u8^l&ccocgjxnpp*zn46s^(z&o65dj-2b-otwj6njyny'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aplicatie',
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

ROOT_URLCONF = 'proiect1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,], #TEMPLATE_DIR este calea catre directorul templates din proiectul nostru
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

WSGI_APPLICATION = 'proiect1.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BcryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 9}, #parola trebuie sa aiba cel putin 9 caractere
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

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    STATIC_DIR, #STATIC_DIR este calea catre directorul static din proiectul nostru
]

MEDIA_ROOT=MEDIA_DIR #MEDIA_DIR este calea catre directorul media din proiectul nostru
MEDIA_URL='/media/' #MEDIA_URL este url-ul pentru directorul media din proiectul nostru

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
