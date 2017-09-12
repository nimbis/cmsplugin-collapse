#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin-collapse',
    version='0.4.1',
    author='Nimbis Services, Inc.',
    author_email='devops@nimbisservices.com',
    url='http://github.com/nimbis/cmsplugin-collapse',
    description=('A simple bootstrap accordion plugin for django-cms'),
    long_description=open('README.md').read(),
    packages=find_packages(exclude=["tests", ]),
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
    install_requires=[
        'Django',
        'django-cms >= 3.3.1',
        'django-sekizai',
    ]
)
