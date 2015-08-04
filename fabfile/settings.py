
# host -> vagrant
vagrant = {
    'inventory': {
        'web': 'ansible/inventory/vagrant/web.ini',
        'db': 'ansible/inventory/vagrant/db.ini',
        'ci': 'ansible/inventory/vagrant/ci.ini'
    }
}

# vagrant -> vagrant
development = {
    'inventory': 'ansible/inventory/development.ini'
}

# ci -> staging
staging = {
    'inventory': 'ansible/inventory/staging.ini'
}

