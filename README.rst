.. image:: https://travis-ci.org/brady-vitrano/django-starter-project.svg?branch=master
    :target: https://travis-ci.org/brady-vitrano/django-starter-project
.. image:: https://readthedocs.org/projects/django-full-stack-kit/badge/?version=latest
    :target: https://readthedocs.org/projects/django-full-stack-kit/?badge=latest
    :alt: Documentation Status    

About
=====
This my attempt at creating and defining best practices for managing a full stack Django application. It focuses on
being simple to run Django in multiple environments with an emphasis on deployments and CI environments.


Requirements
============

* Python PIP
* Fabric  - Task manager used for running CI and Deployments
* Wheel - For packaging dependencies
* Ansible - Config managment and deployment
* ``Vagrant >= 1.7.4``
* ``VirtualBox >= 5.0``
* MySQL client
* NodeJS
* Bower
* Gulp
* Mac/Linux Development Environment

Prepare
=======
Before installation of any pip packages, it is recommended to use a virtual environment such as ``virtualenv`` or ``anaconda``.
I personally use anaconda_.

Assuming you have all above requirements, the following should work and you will be ready for development on local box.

::

    git clone <repo>
    cd <repo>
    pip install -r requirements.txt
    fab install
    # Add server environment variables to ansible/roles/webserver/vars/credentials.yml
    # ./manage.py runserver

Additionally, you can fire up vagrant machines to test deployments and continuous integration pipelines.
::

    vagrant up
    vagrant reload web
    fab build && fab deploy # defaults to vagrant deployment
    fab docs.deploy
    # Visit: https://127.0.0.1:8443, it might take a sec., plus you can run deploy any time
    # Documentation website: http://127.0.0.1:8080


**Warning:** Tested against ``Vagrant 1.7.4``. If you are using older version of Vagrant and you want to keep using it,
you will need to change Vagrant's private key reference in ``ansible/inventory/vagrant.ini`` to use ``~/.vagrant.d/insecure_private_key``

CI Pipeline
-----------

When vagrant provisioning is complete, you will have a CI environment ready for continuous integration. It has a git server
for an alternate `origin` for pushing code changes for continuous integration. Use this server for testing CI pipeline and configurations.
See ``ansible/roles/ci/files/etc/go/cruise-config.xml`` for sample Go.CD pipelines.

Location: ``http://localhost:8153/go/``

Use the following commands to register repo with the CI git server and push to this server to trigger jobs.

::

    git remote add ci ssh://git@127.0.0.1:2201/~/mysite.git
    git push ci master
    git push ci --tags


----------------------------
Vagrant Network Requirements
----------------------------
I am using Vagrants multiple machine for this application.

* web - 8443, 8080
* ci - 8153

Style Guide
===========

See styleguide_

Notable Changes
===============
* See fabfile tasks ``fab --list``
* Added ``ansible`` directory for deployment scripts and ``Vagrant`` provisioning
* Moved ``settings.py`` into ``mysite/settings/__init__.py`` and added additional environments
* Set ``DJANGO_SETTINGS_MODULE=mysite.settings.development`` in ``uwsgi.py``

Notes
=====
* ``git archive --format=tar -o build/archive.tar 1.2.2``
* ``python setup.py sdist``
* ``ansible-playbook -i ansible/inventory/vagrant --private-key=.vagrant/machines/default/virtualbox/private_key -u vagrant --sudo ansible/deploy.yml``
* Build docs for more information

Troubleshooting
===============
*  ``Library not loaded: libssl.1.0.0.dylib`` - Try ``brew install --upgrade openssl && brew unlink openssl && brew link openssl --force``

.. _anaconda: http://continuum.io/downloads
.. _styleguide: styleguide/README.rst
