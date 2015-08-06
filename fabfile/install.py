import os
from glob import glob
from fabric.api import task, local, run, env
from fabric.context_managers import lcd
import settings


@task(default=True)
def project():
    """
    fab install --set environment=ci,python=env/bin/python,pip=env/bin/pip
    """
    try:
        os.makedirs('public')
    except OSError:
        pass
    rax_auth()
    styleguide()
    local('[ -f ansible/roles/webserver/vars/credentials.yml ] || cp ansible/roles/webserver/vars/credentials.example.yml ansible/roles/webserver/vars/credentials.yml')


@task()
def styleguide():
    """
    Install styleguide requirements
    """
    if settings.environment == 'ci':
        local('virtualenv env')
        local('{0} --version'.format(settings.bin['python']))
        local('{0} setup.py install'.format(settings.bin['python']))
        local('{0} install -r requirements.txt'.format(settings.bin['pip']))

    with lcd('styleguide'):
        if settings.environment == 'ci':
            local('git config --global url."https://".insteadOf git://')
        local('{0} install'.format(settings.bin['npm']))
        local('{0} install'.format(settings.bin['bower']))


@task()
def rax_auth():
    """
    Install django rax sso install
    """
    if not os.path.exists('django-rax-auth'):
        local('git clone git@github.rackspace.com:jay7958/django-rax-auth.git')
    local('{0} install django-rax-auth/'.format(settings.bin['pip']))
    local('{0} manage.py migrate'.format(settings.bin['python']))
