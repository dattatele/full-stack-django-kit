from fabric.api import task, local, run
import settings


@task(default=True)
def all():
    """
    (Default) ping; unit; acceptance; integration
    """
    local('python setup.py test')


@task()
def verify():
    local('npm --version')
    local('gulp --version')
    local('bower --version')
    if settings.environment == 'ci':
        local('virtualenv --version')

@task()
def ping():
    """
    Ping servers with ansible Usage: fab test.ping:(vagrant|env)
    """
    if settings.environment == 'vagrant':
        local('ansible webservers -i %s -v -m ping' %
              ('ansible/inventory/vagrant/web.ini'))
        local('ansible databases -i %s -v -m ping' %
              ('ansible/inventory/vagrant/db.ini'))
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
          (settings.inventory, command))

