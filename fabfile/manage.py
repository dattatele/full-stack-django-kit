"""
Ad hoc tasks for managing django application and database
"""

import os
from fabric.api import task, local, run
# Setting for Vagrant
os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'


@task()
def logs():
    """
    Fetch remote logs
    """
    local('ansible webservers --sudo -i ansible/inventory/webservers/vagrant.ini -m fetch -a "dest=logs/{{ inventory_hostname }}-errors.log src=/var/log/nginx/error.log flat=yes"')
    local('ansible webservers --sudo -i ansible/inventory/webservers/vagrant.ini -m fetch -a "dest=logs/{{ inventory_hostname }}-access.log src=/var/log/nginx/access.log flat=yes"')
    local('ansible webservers --sudo -i ansible/inventory/webservers/vagrant.ini -m fetch -a "dest=logs/{{ inventory_hostname }}-wsgi.log src=/var/log/uwsgi/localhost.log flat=yes"')

@task()
def recreatedb():
    """
    Delete database and run manage.py migrate
    """
    local('ansible databases -i ansible/inventory/databases/vagrant.ini -m mysql_db -a "name=demo state=absent"')
    local('ansible databases -i ansible/inventory/databases/vagrant.ini -m mysql_db -a "name=demo state=present collation=utf8_general_ci"')
    local('ansible-playbook --sudo -i ansible/inventory/webservers/vagrant.ini ansible/deploy.yml --tags syncdb')

@task()
def dumpdb():
    """
    Create sql dump on remote and save to local machine dump.sql
    """
    local('ansible databases -i ansible/inventory/databases/vagrant.ini -m mysql_db -a "state=dump name=demo target=/tmp/dump.sql"')
    local('ansible databases -i ansible/inventory/databases/vagrant.ini -m fetch -a "src=/tmp/dump.sql dest=logs/dump.sql flat=yes"')

@task()
def importdb():
    """
    Upload dump.sql to remote and import data to database
    """
    local('ansible databases -i ansible/inventory/databases/vagrant.ini -m copy -a "src=logs/dump.sql dest=/tmp"')
    local('ansible databases -i ansible/inventory/databases/vagrant.ini -m mysql_db -a " name=demo state=import target=/tmp/dump.sql"')

@task()
def generate():
    """
    Generates random data for the database for test purposes
    """
    local("ansible webservers --sudo -i ansible/inventory/webservers/vagrant.ini -m shell -a \"../env/bin/python manage.py generate --settings=mysite.settings.vagrant chdir=/usr/share/nginx/localhost/mysite\"")


