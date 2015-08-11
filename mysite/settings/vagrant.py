from .development import *

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo',
        'USER': 'demo',
        'PASSWORD': 'demo',
        'HOST': '192.168.10.11',
        'PORT': ''
        }
}

# simulate security settings for behind https
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# Handling hsts via nginx
#SECURE_HSTS_SECONDS = 10886400  # Expiry must be at least eighteen weeks (10886400 seconds).
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
# using nginx uwsgi socket therefore xforwarded protocol is empty
#SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")


EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/sentmail'
