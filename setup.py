
import os
import site
import errno
import sys

#qfrom distutils.core import setup, find_packages
from setuptools import setup, find_packages

print(sys.version)

version = "0.0.0"

JYTHON_JAR=""


if __name__ == '__main__':



    setup (
        # basic package data
        name = 'monkeywrench',
        version=version,
        description='MonkeyWrench is a collection of tools for various admin functions.',
        long_description='MonkeyWrench is a collection of tools for various admin functions.',
        keywords='Jython',
        author='Charles Sibbald',
        author_email='casibbald@gmail.com',
        url='',
        license='MIT',

        #package structure
        packages = find_packages(exclude=['ez_setup.py', 'tests']),
                                package_dir = {'monkeywrench/classes':''},
                                zip_safe = False,

        # install your application executable
        install_requires = [
            'docutils',
            'nose',
            'coverage',
            'unittest2'
        ],
        # use this to run tests automatically,
        # but to see coverage report run ~/bin/nosetests -v --with-coverage
        test_suite='nose.collector',
    )
