
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

CI Pipeline
===========
* Pull latest changes
* Run acceptance tests
* Create deployment package
* Deployment::

    sudo mkdir releases/1.1.1
    sudo chown vagrant -R releases/1.1.1
    cd releases/1.1.1
    # tar xvfz mysite-1.1.1.tar.gz
    virtualenv env
    source env/bin/activate
    django-admin startproject mysite # or pip install wheel
    sudo ln -s /usr/share/nginx/releases/1.1.1 /usr/share/nginx/localhost
    sudo touch /etc/uwsgi/configs/localhost.ini

* Bump version via tag
    * fab bump:(major|minor|patch)
* Run deployment


Notable Changes
===============
* Store application requirements in `setup.py`
* Added `fabfile.py` for task manager to be used in CI scripts
* Added `ansible` directory for deployment scripts and `Vagrant` provisioning
* Moved `settings.py` into `mysite/settings/__init__.py` and added additional environments
* Set default `DJANGO_SETTINGS_MODULE` to `mysite.settings.development`

Notes
=====
* `git archive --format=tar -o build/archive.tar 1.2.2`
* `python setup.py sdist`
* `ansible-playbook -i ansible/inventory/vagrant --private-key=.vagrant/machines/default/virtualbox/private_key -u vagrant --sudo ansible/deploy.yml`
