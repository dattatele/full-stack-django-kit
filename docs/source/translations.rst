
Turning On/Off Translations
===========================
Set ``USE_I18N`` to ``True``
Update ``LANGUAGES`` in ``settings/__init__.py``
Add ``mysite.context_processors.i18n`` to ``TEMPLATES`` in ``settings/__init__.py``
Add ``url(r'^i18n/', include('django.conf.urls.i18n'))`` to ``mysite/urls.py``

Requirements
============
::

    brew install gettext
    brew link gettext --force

Create Translation Files then Compile
=====================================
::

    django-admin makemessages -l es --ignore node_modules
    django-admin compilemessages

Resources
=========
http://django.readthedocs.org/en/1.8.x/topics/i18n/translation.html
http://django-rosetta.readthedocs.org/en/latest/index.html
