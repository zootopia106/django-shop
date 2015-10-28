# -*- coding: utf-8 -*-
from __future__ import unicode_literals

SECRET_KEY = 'secret'

INSTALLED_APPS = (
    'django.contrib.auth',
    'email_auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'treebeard',
    'cms',
    'post_office',
    'filer',
    'shop',
    'testshop',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'shop.middleware.CustomerMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

SILENCED_SYSTEM_CHECKS = ['auth.W004']

SHOP_APP_LABEL = 'testshop'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

SERIALIZATION_MODULES = {'shop': 'shop.money.serializers'}

AUTH_USER_MODEL = 'email_auth.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
