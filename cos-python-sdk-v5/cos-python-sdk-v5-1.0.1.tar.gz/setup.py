from setuptools import setup, find_packages
from platform import python_version_tuple


def requirements():

    with open('requirements.txt', 'r') as fileobj:
        requirements = [line.strip() for line in fileobj]

        version = python_version_tuple()

        if version[0] == 2 and version[1] == 6:
            requirements.append("argparse==1.4.0")
        return requirements


def long_description():
    with open('README.rst', 'r') as fileobj:
        return fileobj.read()


setup(
    name='cos-python-sdk-v5',
    version='1.0.1',
    url='https://www.qcloud.com/',
    license='MIT',
    author='tiedu, lewzylu, channingliu',
    author_email='dutie123@qq.com',
    description='cos-python-sdk-v5',
    long_description=long_description(),
    packages=find_packages(),
    install_requires=requirements()
)
