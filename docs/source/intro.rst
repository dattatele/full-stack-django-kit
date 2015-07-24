=======
Welcome
=======
This project was built to experiment with various best practices for building and managing a Django website. The target
audience for this project is an agile team that practices continuous integration and continuous delivery.

This project will strive to be easy to scale using Rackspace and/or AWS.

-------------
Project Goals
-------------

* Support multiple Django settings for various environments
* Provide Requirements for Continuous Integration
* Consistent Builds
* Easy deployments and rollbacks
* Well Documented

--------
Progress
--------
* Created Ansible playbooks for installation, deployment, and rollbacks
* Added Vagrant VM provisioning
* Added Documentation
* Created ``fabfile.py`` for CI pipeline jobs

------------
Technologies
------------

* Ansible - Config management
* Fabric - Task runner
* Sphinx - Documentation
* PyTest - Test Runner
* Ubuntu Trusty - Linux OS
* Nginx - Web Server
* uWSGI - Web Server in Emperor mode


----------------
Incubation Ideas
----------------

* Docker build and deployment strategy
* Database rollbacks
* Infrastructure creation using Rackspace/AWS (Servers, Databases, Load Balancers, Cache, etc)
* Multi-Machine Vagrant for miniature test environment
* Feature flagging
* Log aggregation
* Static and Media file storage in Rackspace Cloud Files and AWS S3
* Multi-Site Hosting same app with different settings ie. staging and testing on same server



