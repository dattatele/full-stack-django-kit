import os
import re
from glob import glob
import shutil
from fabric.api import task, local, run, env
from fabric.context_managers import lcd
import settings


@task()
def test():
    print settings.bin


@task(default=True)
def application():
    """
    (Default) Deploy latest version or specific tag to vagrant. Usage: deploy --set tag=(latest|#.#.#)
    """
    builds = [f for f in os.listdir('dist')
                if re.match(r'\w+-%s(\.tar.gz|.*\.whl)' % settings.version.replace('.', '\.'), f)]
    artifacts = [f for f in os.listdir('ansible/roles/application/files')
                if re.match(r'\w+-%s(\.tar.gz|.*\.whl)' % settings.version.replace('.', '\.'), f)]
    if not builds and not artifacts:
        print 'please build and artifacts for deployment'
        exit(1)

    if not artifacts and builds:
        for package in builds:
            shutil.move(os.path.join('dist', package), os.path.join('ansible/roles/application/files', os.path.basename(package)))
        artifacts = builds

    # all we need are artifacts
    if len(artifacts) != 2:
        print 'failed to find wheel and tar packages for version: %s' % settings.version
        exit(1)
    # Due to how ansible resolves hosts, we cannot reuse a single vagrant.ini
    local('ansible-playbook -i %s --extra-vars "version=%s" -v --sudo ansible/deploy.yml' %
          (settings.inventory, settings.version))

@task()
def rollback():
    """
    Rollback to previous deployed version of the app
    """
    local('ansible-playbook -i %s -v --sudo ansible/rollback.yml' % settings.inventory)


@task()
def provision():
    """
    Run ansible playbook for webservers/databases by env. Usage: deploy.provision:(vagrant|prod)
    """
    if settings.environment == 'vagrant':
        # vagrant ansible playbook for reference, use vagrant provision
        local('ansible-playbook -i ansible/inventory/vagrant/web.ini --sudo --limit webservers ansible/webservers.yml')
        local('ansible-playbook -i ansible/inventory/vagrant/db.ini -v --sudo ansible/dbservers.yml')
    else:
        local('ansible-playbook ansible/main.yml -i {0} --list-hosts'.format(settings.inventory))
