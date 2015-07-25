#!/usr/bin/env python
from __future__ import print_function
import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
import mysite


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

install_requirements = [
    'Django==1.8.3',
    'mysqlclient==1.3.6'
]

setup(
    name='mysite',
    version=mysite.__version__,
    cmdclass={'test': PyTest},
    packages=find_packages(),
    url='https://github.com/brady-vitrano/mysite',
    setup_requires=[],
    install_requires=install_requirements,
    platforms=['any'],
    license='MIT',
    author='brady-vitrano',
    author_email='bjvitrano@gmail.com',
    description='Django demo',
    include_package_data=True,
    tests_require=['pytest', 'pytest-pep8', 'pytest-django', 'pytest-cov',
                   'mock'],
    zip_safe=False
)