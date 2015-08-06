from fabric.api import task, local, run
from fabric.context_managers import lcd
import settings


@task(default=True)
def build():
    """
    (Default) Build Sphinx HTML documentation
    """
    with lcd('docs'):
        if settings.environment == 'ci':
            local('source env/bin/activate')
        local('make html')


@task()
def deploy():
    """
    Upload docs to server
    """
    build()
    destination = '/usr/share/nginx/localhost/mysite/docs/build/html'
    if settings.environment == 'vagrant':
        local("rsync -avz --rsync-path='sudo rsync' -e 'ssh -p 2222 -i .vagrant/machines/web/virtualbox/private_key -o StrictHostKeyChecking=no' docs/build/html/ %s@%s:%s " % ('vagrant', 'localhost', destination))
    elif settings.environment == 'ci':
        local("rsync -avz --rsync-path='sudo rsync' -e 'ssh -p 2222 -i /var/go/id_rsa_web -o StrictHostKeyChecking=no' docs/build/html/ %s@%s:%s " % ('vagrant', '192.168.10.10', destination))

