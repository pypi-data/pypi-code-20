#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'infra-buddy',
        version = '0.1.24',
        description = 'CLI for deploying micro-services',
        long_description = 'CLI for deploying micro-services',
        author = '',
        author_email = '',
        license = 'Apache 2.0',
        url = 'https://github.com/AlienVault-Engineering/infra-buddy',
        scripts = ['scripts/infra-buddy'],
        packages = [
            'infra_buddy',
            'infra_buddy.aws',
            'infra_buddy.commands',
            'infra_buddy.context',
            'infra_buddy.deploy',
            'infra_buddy.template',
            'infra_buddy.utility',
            'infra_buddy.commands.deploy_cloudformation',
            'infra_buddy.commands.deploy_service',
            'infra_buddy.commands.validate_template'
        ],
        namespace_packages = [],
        py_modules = [],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {
            'infra_buddy': ['context/builtin-templates.json']
        },
        install_requires = [
            'click',
            'boto3',
            'pydash',
            'jsonschema',
            'requests'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )
