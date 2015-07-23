Requirements
============

* Vagrant
* Ansible
* Mac/Linux Development Environment


Vagrant Usage
=============
::

    vagrant up
    vagrant reload
    vagrant ssh
    source /usr/share/nginx/localhost/env/bin/activate
    cd /usr/share/nginx/localhost
    sudo chown www-data -R /usr/share/nginx/localhost
    django-admin startproject mysite
    sudo touch /etc/uwsgi/configs/localhost.ini

Build and Deploy
================
Build and deploy latest to Vagrant::

    fab build
    fab deploy:vagrant

Build and deploy a specific version to production assuming ``1.1.1`` package is in proper location::

    fab deploy:prod,1.1.1

**Warning:** ``fab build`` will include any working file changes!

Fabric Tasks
============
* ``fab build``
* ``fab deploy:(vagrant|prod),1.1.1``
* ``fab clean``
* ``fab bump:(major|minor|patch)``

Notable Changes
===============
* Store application requirements in ``setup.py``
* Added ``fabfile.py`` for task manager to be used in CI scripts
* Added ``ansible`` directory for deployment scripts and ``Vagrant`` provisioning
* Moved ``settings.py`` into ``mysite/settings/__init__.py`` and added additional environments
* Set ``DJANGO_SETTINGS_MODULE=mysite.settings.development`` in ``uwsgi.py``

Notes
=====
* ``git archive --format=tar -o build/archive.tar 1.2.2``
* ``python setup.py sdist``
* ``ansible-playbook -i ansible/inventory/vagrant --private-key=.vagrant/machines/default/virtualbox/private_key -u vagrant --sudo ansible/deploy.yml``

