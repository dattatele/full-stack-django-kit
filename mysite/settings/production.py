from mysite.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/usr/share/nginx/db.sqlite3',
        }
}

# temporary key generation
SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['mysite.com']
# Change me if using S3 or Cloud Files
STATIC_URL = '/static/'

# security settings
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 60*60*24
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")


