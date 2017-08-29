"""setuptools setup module for oauth-dropins.

Docs:
https://packaging.python.org/en/latest/distributing.html
http://pythonhosted.org/setuptools/setuptools.html

Based on https://github.com/pypa/sampleproject/blob/master/setup.py
"""
from setuptools import setup, find_packages
from setuptools.command.test import ScanningLoader


class TestLoader(ScanningLoader):
  def __init__(self, *args, **kwargs):
    super(ScanningLoader, self).__init__(*args, **kwargs)
    # webutil/test/__init__.py makes App Engine SDK's bundled libraries importable.
    import oauth_dropins.webutil.test


setup(name='oauth-dropins',
      version='1.8',
      description='Drop-in App Engine OAuth client handlers for many popular sites.',
      long_description=open('README.rst').read(),
      url='https://github.com/snarfed/oauth-dropins',
      packages=find_packages(),
      include_package_data = True,
      author='Ryan Barrett',
      author_email='oauth-dropins@ryanb.org',
      license='Public domain',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: System :: Systems Administration :: Authentication/Directory',
          'Environment :: Web Environment',
          'License :: OSI Approved :: MIT License',
          'License :: Public Domain',
          'Programming Language :: Python :: 2',
      ],
      keywords='oauth appengine',
      # Keep in sync with requirements.txt!
      install_requires=[
          'gdata>=2.0.18',
          'google-api-python-client>=1.6.3',
          'httplib2',
          'oauth2client>=4.1.1',
          'oauthlib',
          'python-tumblpy',
          'requests>=2.10.0',
          'requests-oauthlib',
          'requests-toolbelt>=0.6.2',
          'tweepy>=3.0',
          'beautifulsoup4',
          'mf2py',
          'mf2util',
          'urllib3>=1.14',
      ],
      extras_require={
          'appenginesdk': ['appengine-sdk >= 1.9.40.post0'],
      },
      test_loader='setup:TestLoader',
      test_suite='oauth_dropins.webutil',
)
