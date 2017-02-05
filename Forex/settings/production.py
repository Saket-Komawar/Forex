from django.conf import settings

DATABASES = settings.DATABASES


import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=y@)7!o)-f8$0np*aedi+_=_$u4#e@sndtkp-p9p4@r8n=2=rn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*', 'shielded-thicket-76813.herokuapp.com', ]


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
