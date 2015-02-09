#!/usr/bin/env python

import uuid

from setuptools import find_packages, setup
from pip.req import parse_requirements

# parse requirements
reqs = parse_requirements("requirements/common.txt", session=uuid.uuid1())

setup(
    name='cmsplugin-collapse',
    version='0.2.4',
    author='Nimbis Services, Inc.',
    author_email='devops@nimbisservices.com',
    url='http://github.com/nimbis/cmsplugin-collapse',
    description=('A simple bootstrap accordion plugin for django-cms'),
    long_description=open('README.md').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[str(x).split(' ')[0] for x in reqs]
)
