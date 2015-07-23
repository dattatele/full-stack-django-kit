Requirements
============

* Python PIP
* Fabric ``pip install fabric`` - Task manager used for running CI and Deployments
* PIP wheel ``pip install wheel`` - For packaging dependencies
* Ansible ``pip install ansible`` - Config managment and deployment
* Vagrant
* Mac/Linux Development Environment


Vagrant Usage
=============
::
    vagrant up
    vagrant reload
    fab deploy:vagrant
    # Visit: https://127.0.0.1:8443

**Warning:** It is possible to fail during ``fab deploy`` because of an existing 127.0.0.1:2222 entry in ``~/.ssh/known_hosts``
If you find this entry in your known_hosts file, try deleting the entry and try again.

**Warning:** Tested against ``Vagrant 1.7.4``. If you are using older version of Vagrant and you want to be lazy and not
upgrade. You will need to change Vagrants private key to reference in ``fabfile.py`` to use ``~/.vagrant.d/insecure_private_key``


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
* ``fab provision:(vagrant|prod)``

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

