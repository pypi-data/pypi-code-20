#!/usr/bin/env python
from setuptools import setup

setup(
    author='Chris Sinchok',
    author_email='chris@sinchok.com',
    name='django-webpack-plugin',
    version='0.0.4',
    url='https://github.com/csinchok/django-webpack',
    packages=['webpack', 'webpack.management', 'webpack.management.commands'],
    include_package_data=True
)