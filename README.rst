About
=====
This my attempt at creating and defining best practices for managing a full stack Django application. It focuses on
being simple to run Django in multiple environments with an emphasis on deployments and CI environments.


Requirements
============

* Python PIP
* Fabric ``pip install fabric`` - Task manager used for running CI and Deployments
* Wheel ``pip install wheel`` - For packaging dependencies
* Ansible ``pip install ansible`` - Config managment and deployment
* ``Vagrant >= 1.7.4``
* Mac/Linux Development Environment

Prepare
=======
Before installation of any pip packages, it is recommended to use a virtual environment such as ``virtualenv`` or ``anaconda``.
I personally use anaconda_.

::

    git clone <repo>
    pip install -r requirements.txt # for now, installs fabric, ansible, and wheel

Vagrant Usage
=============
::

    export ANSIBLE_HOST_KEY_CHECKING=False # vagrant requirement only
    vagrant up
    vagrant reload
    fab deploy:vagrant
    # Visit: https://127.0.0.1:8443, it might take a sec., plus you can run deploy again

**Warning:** Tested against ``Vagrant 1.7.4``. If you are using older version of Vagrant and you want to keep using it,
you will need to change Vagrant's private key reference in ``fabfile.py`` to use ``~/.vagrant.d/insecure_private_key``

---------------
Vagrant Network
---------------
I am using Vagrants multiple machine for this application.

VM List and Details

* **web**
    * **IP** 192.168.10.10
    * **Ports**
        * **SSH** guest: 22 host: 2222
        * **Nginx** guest: 443 host: 8443
        * **Nginx** guest: 80 host: 8080
* **db**
    * **IP** 192.168.10.11
    * **Ports**
        * **SSH** guest: 22 host: 2200

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
* ``fab deploy:(vagrant|prod)[,version]``
* ``fab clean``
* ``fab bump:(major|minor|patch)``
* ``fab provision:(vagrant|prod)``
* ``fab ping:vagrant``
* ``fab docs``
* ``fab test``



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


.. _anaconda: http://continuum.io/downloads