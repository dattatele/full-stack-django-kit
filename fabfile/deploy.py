import os
import re
from glob import glob
from fabric.api import task, local, run
from fabric.context_managers import lcd
from mysite.version import get_git_version
from build import create_package


@task(default=True)
def vagrant(ver='latest'):
    """
    (Default) Deploy latest version or specific tag to vagrant. Usage: deploy.vagrant:(latest|#.#.#)
    """
    if ver == 'latest':
        create_package()
        ver = get_git_version()

    packages = [f for f in os.listdir('ansible/roles/application/files') if re.match(r'\w+-%s(\.tar.gz|.*\.whl)' % ver.replace('.', '\.'), f)]
    if len(packages) != 2:
        print 'failed to find packages for version: %s' % ver
        exit(1)

    local('ansible-playbook -i ansible/inventory/webservers/vagrant.ini --extra-vars "version=%s" --private-key=.vagrant/machines/web/virtualbox/private_key -u vagrant -v --sudo ansible/deploy.yml' % ver)


def production(ver='latest'):
    """
    Deploy latest version or specific tag to production. Usage: deploy.production:(latest|#.#.#)
    """
    if ver == 'latest':
        create_package()
        ver = get_git_version()

    packages = [f for f in os.listdir('ansible/roles/application/files') if re.match(r'\w+-%s(\.tar.gz|.*\.whl)' % ver.replace('.', '\.'), f)]
    if len(packages) != 2:
        print 'failed to find packages for version: %s' % ver
        exit(1)

    local('ansible-playbook ansible/deploy.yml -i ansible/inventory/production.ini --list-hosts')


@task()
def rollback():
    """
    Rollback to previous deployed version of the app
    """
    local('ansible-playbook -i ansible/inventory/webservers/vagrant.ini --private-key=.vagrant/machines/web/virtualbox/private_key -u vagrant -v --sudo ansible/rollback.yml')


@task()
def provision(env):
    """
    Run ansible playbook for webservers/databases by env. Usage: deploy.provision:(vagrant|prod)
    """
    if env == 'vagrant':
        # vagrant ansible playbook for reference, use vagrant provision
        local('ansible-playbook -i ansible/inventory/webservers/vagrant.ini --extra-vars "django_module_settings=mysite.settings.vagrant" --private-key=.vagrant/machines/web/virtualbox/private_key -u vagrant -v --sudo --limit webservers ansible/webservers.yml')
        local('ansible-playbook -i ansible/inventory/databases/vagrant.ini --private-key=.vagrant/machines/db/virtualbox/private_key -u vagrant -v --sudo ansible/dbservers.yml')
    elif env == 'prod':
        local('ansible-playbook ansible/main.yml -i ansible/inventory/production.ini --list-hosts')
