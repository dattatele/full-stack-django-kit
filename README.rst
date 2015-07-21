
CI Pipeline
* Pull latest changes
* Run acceptance tests
* Create deployment package
* Deployment
    * Upload source to destination
    * Create new virtualenv
* Bump version via tag
    * fab bump:(major|minor|patch)
* Run deployment
