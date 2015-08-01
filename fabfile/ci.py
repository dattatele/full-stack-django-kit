from glob import glob
from fabric.api import task, local, run, env
from fabric.context_managers import lcd

@task()
def verify():
    """
    PENDING
    """
    local('npm --version')
    local('gulp --version')
    local('bower --version')


