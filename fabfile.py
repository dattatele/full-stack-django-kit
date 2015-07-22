from fabric.api import local
from mysite.version import get_git_version
from glob import glob


def test():
    local('python manage.py test')


def build():
    local('python manage.py collectstatic --noinput')
    local('python setup.py sdist bdist_wheel')


def get_build_files():
    return glob('dist/*-%s*' % get_git_version())


def package():
    local('')


def deploy(env):
    if env == 'prod':
        local('ansible-playbook ansible/main.yml -i ansible/inventory/production.ini --list-hosts')
    elif env == 'vagrant':
        local('ansible-playbook -i ansible/inventory/vagrant --private-key=.vagrant/machines/default/virtualbox/private_key -u vagrant --sudo ansible/deploy.yml')


def clean():
    local('rm -f dist/*.tar.gz')
    local('rm -f dist/*.whl')


def version():
    print get_git_version()


def bump(component):
    if component not in ['major', 'minor', 'patch']:
        print 'invalid component name valid options: [major|minor|patch]'
        exit(1)
    value = get_git_version()
    components = value.split('.')[:3]
    if len(components) != 3:
        print 'invalid version'
        exit(1)
    components = map(int, components)
    if component == 'major':
        components = [components[0] + 1, 0, 0]
    elif component == 'minor':
        components = [components[0], components[1] + 1, 0]
    elif component == 'patch':
        components = [components[0], components[1], components[2] + 1]
    tag = '.'.join(map(str, components))
    local('git tag -a %s -m "chore(version): bump %s"' % (tag, component))

