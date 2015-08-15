===================
Email Configuration
===================

See respective environment settings file for edits ``mysite.settings.*``. Here are the defaults

Development
-----------
Emails will be printed to stdout.
::

    # mysite/settings/development.py
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


Test
----
Emails will be faked.
::
    # mysite/settings/test.py
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

Vagrant
-------
Emails will be save on the vagrant server.
::
    # mysite/settings/vagrant.py
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = 'tmp/sentmail'


Production
----------
Uses SMTP, you should edit these settings for your send server.

::

    # mysite/settings/production.py
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = None
    EMAIL_PORT = None
    EMAIL_HOST_USER = None
    EMAIL_HOST_PASSWORD = None
    EMAIL_USE_TLS = None
    EMAIL_USE_SSL = None
    EMAIL_TIMEOUT = None
    EMAIL_SSL_KEYFILE = None
    EMAIL_SSL_CERTFILE = None

Resources
---------
MailGun see Django Mailgun App: https://github.com/BradWhittington/django-mailgun

