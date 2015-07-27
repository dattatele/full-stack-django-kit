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
* MySQL client
* Mac/Linux Development Environment

Style Guide Requirements
========================
These requirements are required if you are going to run style guide builds using ``gulp`` via ``fab build.styleguide``.

* NodeJS
* Bower
* Gulp

Prepare
=======
Before installation of any pip packages, it is recommended to use a virtual environment such as ``virtualenv`` or ``anaconda``.
I personally use anaconda_.

Assuming you have all above requirements, the following should work:

::

    git clone <repo>
    pip install -r requirements.txt # for now, installs fabric, ansible, and wheel
    cd styleguide
    npm install
    bower install
    cd ..
    fab build.styleguide

Vagrant Usage
=============
::

    export ANSIBLE_HOST_KEY_CHECKING=False # vagrant requirement only
    vagrant up
    vagrant reload
    fab deploy.vagrant
    # Visit: https://127.0.0.1:8443, it might take a sec., plus you can run deploy again

**Warning:** Tested against ``Vagrant 1.7.4``. If you are using older version of Vagrant and you want to keep using it,
you will need to change Vagrant's private key reference in ``fabfile/deploy.py`` to use ``~/.vagrant.d/insecure_private_key``

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


Fabric Tasks
============
Tasks for CI/CD pipelines.

When building/deploying, you can alter django settings module with fabric's set option ``fab ... --set settings=mysite.settings``

::

    $ fab --list
    Available commands:

        build             (Default) Peforms makemigrations and collectstatic then packages with sdist and bdist_wheel
        build.bump        Bump git tag. Usage: build.bump:(major|minor|patch)
        build.clean       Remove build files and directories
        build.package     (Default) Peforms makemigrations and collectstatic then packages with sdist and bdist_wheel
        build.styleguide  Run gulp build task in styleguide for creating minified CSS and JS
        deploy            (Default) Deploy latest version or specific tag to vagrant. Usage: deploy.vagrant:(latest|#.#.#)
        deploy.provision  Run ansible playbook for webservers/databases by env. Usage: deploy.provision:(vagrant|prod)
        deploy.rollback   Rollback to previous deployed version of the app
        deploy.vagrant    (Default) Deploy latest version or specific tag to vagrant. Usage: deploy.vagrant:(latest|#.#.#)
        docs              (Default) Build Sphinx HTML documentation
        docs.build        (Default) Build Sphinx HTML documentation
        docs.deploy       PENDING: should upload to docs server
        test              (Default) ping; unit; acceptance; integration
        test.acceptance   PENDING: Perform acceptance tests (pep8)
        test.all          (Default) ping; unit; acceptance; integration
        test.integration  PENDING: Run integration tests for specific environments
        test.ping         Ping servers with ansible Usage: fab test.ping:(vagrant|env)
        test.unit         Perform unit tests via python setup.py test


Style Guide
===========

See styleguide_

Notable Changes
===============
* Store application requirements in ``setup.py``
* Added ``fabfile`` module for task manager to be used in CI scripts
* Added ``ansible`` directory for deployment scripts and ``Vagrant`` provisioning
* Moved ``settings.py`` into ``mysite/settings/__init__.py`` and added additional environments
* Set ``DJANGO_SETTINGS_MODULE=mysite.settings.development`` in ``uwsgi.py``

Notes
=====
* ``git archive --format=tar -o build/archive.tar 1.2.2``
* ``python setup.py sdist``
* ``ansible-playbook -i ansible/inventory/vagrant --private-key=.vagrant/machines/default/virtualbox/private_key -u vagrant --sudo ansible/deploy.yml``


.. _anaconda: http://continuum.io/downloads
.. _styleguide: styleguide/README.rst