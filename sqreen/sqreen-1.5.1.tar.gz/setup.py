# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


metadata = {}
with open("sqreen/metadata.py") as fp:
    exec(fp.read(), metadata)


long_description = """Sqreen is a SaaS based Application protection and monitoring platform that integrates directly into your Python applications.
Learn more at `<https://www.sqreen.io/>`_."""


setup(
    name='sqreen',
    version=metadata['__version__'],
    description="Sqreen agent to protect Python applications.",
    long_description=long_description,
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    url='https://www.sqreen.io/',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={'sqreen':
                 'sqreen'},
    package_data={'sqreen': ['*.crt', 'rules_callbacks/*.html']},
    include_package_data=True,
    install_requires=[
        'py-mini-racer>=0.1.10',
    ],
    license=metadata['__license__'],
    zip_safe=False,
    keywords='sqreen',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
    ],
    test_suite='tests',
    tests_require=[],
    entry_points={
        'console_scripts': [
            "sqreen-start = sqreen.bin.protect:protect"
        ]
    }
)
