from fabric.api import task, local, run
from fabric.context_managers import lcd


@task(default=True)
def build():
    """
    (Default) Build Sphinx HTML documentation
    """
    with lcd('docs'):
        local('make html')


@task()
def deploy(environment='vagrant'):
    """
    Upload docs to server
    """
    build()
    if environment == 'vagrant':
        destination = '/usr/share/nginx/localhost/mysite/docs/build/html'
        local("rsync -avz --rsync-path='sudo rsync' -e 'ssh -p 2222 -i .vagrant/machines/web/virtualbox/private_key -o StrictHostKeyChecking=no' docs/build/html/ %s@%s:%s " % ('vagrant', 'localhost', destination))
