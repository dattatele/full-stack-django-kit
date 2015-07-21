
CI Pipeline
===========
* Pull latest changes
* Run acceptance tests
* Create deployment package
* Deployment
    * Upload source to destination
    * Create new virtualenv
* Bump version via tag
    * fab bump:(major|minor|patch)
* Run deployment


Notable Changes
===============
* Store application requirements in `setup.py`
* Added `fabfile.py` for task manager to be used in CI scripts
* Added `ansible` directory for deployment scripts and `Vagrant` provisioning
* Moved `settings.py` into `mysite/settings/__init__.py` and added additional environments
* Set default settings to `mysite.settings.development`

