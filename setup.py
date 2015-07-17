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
    'Django==1.8.3'
]

setup(
    name='mysite',
    version=mysite.__version__,
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    packages=find_packages(),
    url='https://github.com/brady-vitrano/mysite',
    setup_requires=["setuptools-git==1.1"],
    install_requires=install_requirements,
    platforms=['any'],
    license='MIT',
    author='brady-vitrano',
    author_email='bjvitrano@gmail.com',
    description='Django demo',
    include_package_data=True,
    extras_require={
        'testing': ['pytest'],
    },
    zip_safe=False
)