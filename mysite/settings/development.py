from mysite.settings import *

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