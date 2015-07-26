from glob import glob
from fabric.api import task, local, run
from fabric.context_managers import lcd
from mysite.version import get_git_version


def get_build_files():
    return glob('dist/*-%s*' % get_git_version())

def create_package():
    local('python manage.py makemigrations')
    local('python manage.py collectstatic --noinput')
    local('python setup.py sdist bdist_wheel')
    files = get_build_files()
    local('mv %s ansible/roles/application/files/' % ' '.join(files))

@task(default=True)
def package():
    """
    (Default) Peforms makemigrations and collectstatic then packages with sdist and bdist_wheel
    """
    create_package()


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


@task()
def styleguide():
    """
    Run gulp build task in styleguide for creating minified CSS and JS
    """
    with lcd('styleguide'):
        local('gulp build')