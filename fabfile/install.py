import os
from glob import glob
from fabric.api import task, local, run, env
from fabric.context_managers import lcd


@task(default=True)
def project():
    try:
        os.mkdir('public')
    except OSError:
        pass
    styleguide()
    local('[ -f ansible/roles/webserver/vars/credentials.yml ] || cp ansible/roles/webserver/vars/credentials.example.yml ansible/roles/webserver/vars/credentials.yml')


@task()
def styleguide():
    """
    Install styleguide requirements
    """
    with lcd('styleguide'):
        local('npm install')
        local('bower install')
        local('gulp build')

