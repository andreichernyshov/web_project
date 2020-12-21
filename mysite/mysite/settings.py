"""
Django settings for mysite project.
Generated by 'django-admin startproject' using Django 3.1.4.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o#a9zj!alalh-%yjo(&%q(-^y8$)%ogzy-%1e!wtr1lwhkqy$k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# Добовляем сюда НАШИ приложения, созданные коммандой startapp [имя_приложения].
# *** Добовляем согласно имени приложения и его пути относительно верхнего уровня (уровень dir[mysite])
# как пример для 'polls' это = dir[polls].class[apps].func(method)[PollsConfig], < это запятая, так надо.
# Выглядит это как наследование/переопределение некой функции(метода) PollsConfig из класса apps, наследуемого
# от класса polls... Хотя PollsConfig - это созданный нами класс, наследуемый от AppConfig из ядра Django
# функции (методы), которого мы наследуем... все чтоли, а определяем лишь аттребут для нашего
# PollsConfig класса name='polls'... надо разбираться, сразу не очень понятно.


# По-умолчанию список содержит ряд выгружаемых приложений из ядра Django, запускаемых при
# каждой команде runserver. Каждое такое приложение содержит в себе код (прописанный в ядре Django)
# с готовыми для него моделями, сценариями, шаблонами, маршрутизацией к ним итд... эти классы тянет
# ядро Django после нашей комманда django-admin startproject.
# Они необходимы для запуска manage.py startserver Django, и собственно позволяют совершать манипуляции
# для manage.py что-бы был доступ к админке, создания пользователей, СУБД итд... а так-же для создания наших
# приложений manage.py startapp, в которые ядро подгрузит ряд базовых шаблонов (в виде модулей .py) как пакет
# для прироления, в них уже будем писать свою логику, маршрутизацию, если нужно тесты итд + дополнять пакет, своми
# модулями, которые посчитаем нужными добавить в наше приложение... как-то так.


INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# НЕ путай Unix-socket с туннелем, снова запоришь все;
# Unix-socket с аттрибутом 's' и 3 восьмеричных... работает как МКАД
# Туннель с аттрибудтом 'p' и 3 восьмеричных... работает как односторонка, таких нужно 2шт.
# комманда "nc" -U [asd.sock]= подключит к файлу сокета, просто убей его маску "umask" а не лезь в конфиги бд
# вообще делай в SQLite пока не разберешься...


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
