========
Workflow
========

:doc:`contributing`

Developer Pipeline

New Branch
Source Code Edits
Push changes (frequently)
acceptance tests
    unit
    code analysis


fab test.acceptance

Prebuild Smoke Tests
Minimum set of tests to verify software is ready for build
- are all requirements satisfied

Postbuild Smoke Tests
- verify infrastructure
- verify connectivity to other systems
-

Environments
------------

Development
Test
Staging
Integration
Production


Marking tests for different environments
@pytest.mark.env("smoke")


Tests
-----
@pytest.mark.integration

Py Test
Recognized Markers
- smoke, integration, ...

Production
----------
Configuration python manage.py check --deploy --settings=mysite.settings.production


Dev Machine -> VagrantWeb
Dev Machine -> VagrantDb
Dev Machine -> VagrantCI
VagrantCI -> VagrantWeb
VagrantCI -> VagrantDb