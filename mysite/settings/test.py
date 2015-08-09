from mysite.settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'