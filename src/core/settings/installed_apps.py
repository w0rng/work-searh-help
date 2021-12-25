from django.conf import settings


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'django_filters',
    'bootstrap4',

    'apps.module',
    'apps.user',
    'siteq.pages',
    'apps.promocode',
    'apps.resume',
    'apps.vacancy',
    'apps.subscription',   
]

if settings.DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
