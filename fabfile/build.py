import os
from glob import glob
from fabric.api import task, local, run, env
from fabric.context_managers import lcd
import settings


@task(default=True)
def package():
    """
    (Default) Peforms gulp build, collectstatic, and sdist and bdist_wheel. fab build --set python=env/bin/python,settings=mysite.settings.development,environment=ci
    """
    try:
        os.makedirs('public')
    except:
        pass
    clean()
    styleguide()
    local('{0} manage.py collectstatic --noinput --clear --settings={1}'.format(settings.bin['python'], settings.django['settings']))
    local('{0} setup.py sdist bdist_wheel'.format(settings.bin['python']))


@task()
def clean():
    """
    Remove build files and directories
    """
    local('rm -f dist/*.tar.gz')
    local('rm -f dist/*.whl')
    local('rm -rf build')
    local('rm -rf .eggs')

@task()
def bump(component):
    """
    Bump git tag. Usage: build.bump:(major|minor|patch)
    """
    if component not in ['major', 'minor', 'patch']:
        print 'invalid component name valid options: [major|minor|patch]'
        exit(1)
    value = settings.version
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


@task()
def styleguide():
    """
    Run gulp build task in styleguide for creating minified CSS and JS
    """
    with lcd('styleguide'):
        local('{0} build'.format(settings.bin['gulp']))

@task()
def watch():
    """
    Run gulp build task in styleguide for creating minified CSS and JS
    """
    with lcd('styleguide'):
        local('{0} watch'.format(settings.bin['gulp']))

