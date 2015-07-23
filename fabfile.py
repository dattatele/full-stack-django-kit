from fabric.api import local
from mysite.version import get_git_version
from glob import glob
import os
import re


def test():
    local('python manage.py test')


def build():
    local('python manage.py makemigrations')
    local('python manage.py collectstatic --noinput')
    local('python setup.py sdist bdist_wheel')
    files = get_build_files()
    local('mv %s ansible/roles/application/files/' % ' '.join(files))


def get_build_files():
    return glob('dist/*-%s*' % get_git_version())


def package():
    local('')


def provision(env):
    # for reference
    if env == 'vagrant':
        # vagrant ansible playbook for reference, use vagrant provision
        local('ansible-playbook -i ansible/inventory/vagrant --extra-vars "django_module_settings=mysite.settings.development" --private-key=.vagrant/machines/default/virtualbox/private_key -u vagrant -v --sudo ansible/main.yml')
    elif env == 'prod':
        local('ansible-playbook ansible/main.yml -i ansible/inventory/production.ini --list-hosts')


def deploy(env, ver='latest'):
    if ver == 'latest':
        build()
        ver = get_git_version()

    packages = [f for f in os.listdir('ansible/roles/application/files') if re.match(r'\w+-%s(\.tar.gz|.*\.whl)' % ver.replace('.', '\.'), f)]
    if len(packages) != 2:
        print 'failed to find packages for version: %s' % ver
        exit(1)

    if env == 'prod':
        local('ansible-playbook ansible/deploy.yml -i ansible/inventory/production.ini --list-hosts')
    elif env == 'vagrant':
        local('ansible-playbook -i ansible/inventory/vagrant --extra-vars "version=%s" --private-key=.vagrant/machines/default/virtualbox/private_key -u vagrant -v --sudo ansible/deploy.yml' % ver)


def clean():
    local('rm -f dist/*.tar.gz')
    local('rm -f dist/*.whl')
    local('rm -rf build')
    local('rm -rf .eggs')


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

