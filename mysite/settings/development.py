from mysite.settings import *

# Add styleguide/dist directory
STATICFILES_DIRS += (
    os.path.join(BASE_DIR, 'styleguide', 'dist'),
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Create log directory if not already found
try:
    os.mkdir(os.path.join(BASE_DIR, 'logs'))
except OSError:
    pass

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'sql': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/sql.log',
            },
        },
    'loggers': {
        'django.db.backends': {
            'handlers': ['sql'],
            'level': 'DEBUG',
            'propagate': True,
            },
        },
    }

