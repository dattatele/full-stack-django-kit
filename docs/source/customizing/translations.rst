
Managing Translations
=====================


Requirements
------------
We are using the GNU's `gettext`_ for creating messages and compiling translations.

::

    brew install gettext
    brew link gettext --force


Django Settings
---------------

::

    # file: settings/__init__.py
    USE_I18N = True
    # Set Support Languages
    LANGUAGES = ()
    # Add Custom context processor
    TEMPLATES = [
        {
            # ...
            'OPTIONS': {
                'context_processors': [
                    # ...,
                    'mysite.context_processors.i18n',
                ],
            },
        },
    ]

Add ability for users to switch between languages
::

    # file: mysite/urls.py
    urlpatterns = [
        # ...
        url(r'^i18n/', include('django.conf.urls.i18n')),
    ]


Create Translation Files then Compile
-------------------------------------
::

    django-admin makemessages -l es --ignore node_modules
    django-admin compilemessages

Resources
---------
- http://django.readthedocs.org/en/1.8.x/topics/i18n/translation.html
- http://django-rosetta.readthedocs.org/en/latest/index.html

.. _gettext: http://www.gnu.org/software/gettext/