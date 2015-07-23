from mysite.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/usr/share/nginx/db.sqlite3',
        }
}

SECRET_KEY = '[REPLACE ME WITH REAL SECRET KEY]'
DEBUG = False
ALLOWED_HOSTS = ['mysite.com']
# Change me if using S3 or Cloud Files
STATIC_URL = '/static/'

