

import os.path
from setuptools import setup, find_packages
from distutils.command.install_scripts import install_scripts
import ssl
# from version import tag_version

# ssl._create_default_https_context = ssl._create_unverified_context
# python setup.py sdist  -k -v  --dry-run

# python setup.py --dry-run --verbose install
# python setup.py install --record files.txt

from distutils.core import setup

version = '0.1.20170829'

setup(
    name='whoshere',
    version=version,
    author='Peter Shipley',
    author_email='Peter.Shipley@gmail.com',
    packages=['whoshere'],
    # packages=find_packages(),
    scripts=['whoshere-isy/whoshere-isy.py', 'whoshere-iftt/whoshere-iftt.py'],
    url='https://github.com/evilpete/whoshere',
    # git='https://github.com/evilpete/whoshere.git',
    description='A program and library to monitor hosts on local network and trigger user defined events via a python callback method',
    license='BSD',
    download_url='https://github.com/evilpete/whoshere/archive/0.1.20170829.tar.gz',
    # long_description=open('README.txt').read(),
    # cmdclass = { 'install_scripts': install_scripts_and_symlinks }
    install_requires=['scapy', 'requests'],
    entry_points={
          'console_scripts': [
              # 'whoshere-isy = whoshere.whoshere_isy:main',
              'whoshere = whoshere.whoshere_main:main'
          ],
      }
)

