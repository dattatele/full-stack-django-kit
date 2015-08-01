from glob import glob
from fabric.api import task, local, run, env
from fabric.context_managers import lcd
from build import styleguide, package

@task()
def verify():
    """
    PENDING
    """
    local('npm --version')
    local('gulp --version')
    local('bower --version')
    local('virtualenv --version')


@task()
def install():
    """
    PENDING
    """
    local('virtualenv env')
    local('env/bin/python --version')

    with lcd('styleguide'):
        local('npm install')
        local('bower install')


@task()
def build():
    """
    PENDING
    """
    styleguide()
    package()
