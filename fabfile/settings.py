import os
from glob import glob
from mysite.version import get_git_version
from fabric.api import env

# --set tag=1.1.1
version = env.get('tag', 'latest')
if version == 'latest':
    version = get_git_version()

# verify version
def get_build_files():
    return glob('dist/*-%s*' % version)

# vagrant, development, ci, testing, staging, production
environment = env.get('environment', 'vagrant')
if environment == 'vagrant' or environment == 'ci':
    os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'

bin = {
    'python': env.get('python', 'python'),
    'pip': env.get('pip', 'pip'),
    'gulp': env.get('gulp', 'gulp'),
    'npm': env.get('npm', 'npm'),
    'bower': env.get('bower', 'bower')
}

defaults = {
    'vagrant': {
        'ansible': {
            'inventory': 'ansible/inventory/vagrant/web.ini'
        },
        'django': {
            'settings': 'mysite.settings.vagrant'
        }
    },
    'development': {
        'ansible': {
            'inventory': 'ansible/inventory/development.ini'
        },
        'django': {
            'settings': 'mysite.settings.development'
        }
    },
    'ci': {
        'ansible': {
            'inventory': 'ansible/inventory/ci.ini'
        },
        'django': {
            'settings': 'mysite.settings.development'
        }
    },
    'staging': {
        'ansible': {
            'inventory': 'ansible/inventory/staging.ini'
        },
        'django': {
            'settings': 'mysite.settings.staging'
        }
    },
    'production': {
        'ansible': {
            'inventory': 'ansible/inventory/production.ini'
        },
        'django': {
            'settings': 'mysite.settings.production'
        }
    }
}

# --set settings=module.settings
django = {
    'settings': env.get('settings', defaults[environment]['django']['settings'])
}

# --set environment=ci,inventory=ansible/inventory/vagrant/ci.ini
inventory = env.get('inventory', defaults[environment]['ansible']['inventory'])

# fab deploy --set environment=ci,inventory=ansible/inventory/development.ini
# fab build --set environment=development,python=env/bin/python,pip=env/bin/pip
