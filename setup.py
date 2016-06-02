#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

from setuptools.command.test import test as TestCommand
from setuptools import setup


class PyTest(TestCommand):
    def __init__(self, *args, **kwargs):
        super(PyTest, self).__init__(*args, **kwargs)
        self.test_suite = True

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        raise SystemExit(errno)


with codecs.open('README.md', encoding='utf8') as readme_file:
    LONG_DESCRIPTION = README = readme_file.read()

with open('requirements.txt') as requirements_file:
    INSTALL_REQUIRES = list(set(
        requirement.strip()
        for requirement in requirements_file
    ))

# updated by bumpversion
VERSION = '0.3.0'

setup(
    name='hydrachain',
    version=VERSION,
    description='Permissioned Distributed Ledger based on Ethereum',
    long_description=LONG_DESCRIPTION,
    author='HeikoHeiko',
    author_email='heiko@brainbot.com',
    url='https://github.com/HydraChain/hydrachain',
    packages=[
        'hydrachain',
        'hydrachain.consensus',
        'hydrachain.examples',
        'hydrachain.examples.native',
        'hydrachain.examples.native.fungible',
    ],
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    keywords='hydrachain',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    cmdclass={'test': PyTest},
    install_requires=INSTALL_REQUIRES,
    tests_require=[
        'docker-compose==1.7.0',
        'bumpversion==0.5.3',
        'pytest==2.9.1'
    ],
    entry_points={
        'console_scripts': [
            'hydrachain = hydrachain.app:app'
        ]
    }
)
