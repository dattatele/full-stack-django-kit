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
def deploy():
    """
    PENDING: should upload to docs server
    """
    print 'pending docs deployment script'

