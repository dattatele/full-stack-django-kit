from fabric.api import task, local, run
import settings


@task(default=True)
def all():
    """
    (Default) ping; unit; acceptance; integration
    """
    local('python setup.py test')


@task()
def ping(env):
    """
    Ping servers with ansible Usage: fab test.ping:(vagrant|env)
    """
    if env == 'vagrant':
        local('ansible webservers -i %s -v -m ping' %
              (settings.vagrant['inventory']['web']))
        local('ansible databases -i %s -v -m ping' %
              (settings.vagrant['inventory']['db']))
    else:
        print 'Not yet created for production env'


@task()
def unit():
    """
    Perform unit tests via python setup.py test
    """
    local('python setup.py test')


@task()
def acceptance():
    """
    PENDING: Perform acceptance tests (pep8)
    """
    unit()


@task()
def integrations():
    """
    Run integration tests by environment via ./manage.py integration
    """
    command = '../env/bin/python manage.py integration --settings=mysite.settings.vagrant'
    local("ansible webservers --sudo -i %s -m shell -a \"%s chdir=/usr/share/nginx/localhost/mysite\"" %
          (settings.vagrant['inventory']['web'], command))

