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

    'apps.user',
    'pages',
    'apps.promocode'
]

if settings.DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
