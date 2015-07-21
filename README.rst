


CI Pipeline
===========
* Pull latest changes
* Run acceptance tests
* Create deployment package
* Deployment
    * Upload source and wheel to destination
    * Create new virtualenv
    * Install wheel to env
    * Install source
        * Move static files to proper destination
* Bump version via tag
    * fab bump:(major|minor|patch)
* Run deployment


Notable Changes
===============
* Store application requirements in `setup.py`
* Added `fabfile.py` for task manager to be used in CI scripts
* Added `ansible` directory for deployment scripts and `Vagrant` provisioning
* Moved `settings.py` into `mysite/settings/__init__.py` and added additional environments
* Set default `DJANGO_SETTINGS_MODULE` to `mysite.settings.development`

Notes
=====
* `git archive --format=tar -o build/archive.tar 1.2.2`
* `python setup.py sdist`
