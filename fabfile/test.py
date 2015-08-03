from fabric.api import task, local, run


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
        local('ansible webservers -i ansible/inventory/webservers/vagrant.ini --private-key=.vagrant/machines/web/virtualbox/private_key -u vagrant -v -m ping')
        local('ansible databases -i ansible/inventory/databases/vagrant.ini --private-key=.vagrant/machines/db/virtualbox/private_key -u vagrant -v -m ping')
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
    local("ansible webservers --sudo -i ansible/inventory/webservers/vagrant.ini -m shell -a \"../env/bin/python manage.py integration --settings=mysite.settings.vagrant chdir=/usr/share/nginx/localhost/mysite\"")

