from distutils.core import setup

setup(
    name="password_gen",
    packages=['password_gen'],
    version="0.1.1",
    description="Generates memorable strong passwords.",
    author='Olu Gbadebo',
    author_email='odgbadeb@asu.edu',
    url='https://github.com/weirdestnerd/password-generator',
    keywords=['password-generator', 'passwords', 'generator'],
    long_description=open('README.md').read(),
    install_requires=[
	'linecache'
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Testing',
    ]
)
