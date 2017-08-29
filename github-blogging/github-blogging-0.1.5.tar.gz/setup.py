#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
from blogging import __VERSION__
from setuptools.command.install import install
import os


def enable_argcomplete():
    with open(os.path.join(os.path.expanduser("~"), '.zshrc'), 'a') as f:
        f.write('\neval "$(register-python-argcomplete blogging)"\n')


class CustomInstallCommand(install):
    """Customized setuptools install command"""

    def run(self):
        install.run(self)
        enable_argcomplete()


setuptools.setup(
    name='github-blogging',
    version=__VERSION__,
    description='A cmdline tool to help managing your blogs',
    packages=['blogging'],
    author='Curtis Yu',
    author_email='icyarm@icloud.com',
    install_requires=[
        'argcomplete',
        'tabulate',
        'termcolor',
    ],
    url='https://github.com/cuyu/blogging',
    entry_points={
        "console_scripts": [
            "blogging = blogging.blogging:main",
        ],
    },
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2'
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
