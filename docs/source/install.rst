
::

    fatal: [127.0.0.1] => SSH Error: Host key verification failed.
        while connecting to 127.0.0.1:2222
    It is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.

``export ANSIBLE_HOST_KEY_CHECKING=False # vagrant requirement only``
