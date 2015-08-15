Testing
=======

Unit and Functional
-------------------

The kit uses ``python setup.py test`` for running tests. The test runner is ``py.test`` and it uses
``fabric`` for managing all the tests.

For other ``fabric`` tasks, the kit uses Ansible for testing server configs and database connectivity.

By Environment
--------------

::

    fab test.settings
    fab test.unit
    fab test.servers
    fab test.databases
    fab test.integrations

