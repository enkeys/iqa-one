# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

from setuptools import setup, find_packages

setup(
    name='iqa-one',
    version='0.1.2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    license='Apache 2.0',
    description='Messaging testing project',
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest', 'pytest-docker', 'nest_asyncio', 'pytest-asyncio', 'mock', 'pytest-mock', 'tox', ],
    install_require=[
        'asyncssh'
        'requests',
        'PyYAML',
        'cython',
        'ansible',
        'python-qpid-proton',
        'amqcfg',
        'dpath',
        'optconstruct',
        'docker',
        'urllib3',
        'kubernetes'
    ],
    url='https://github.com/enkeys/iqa-one',
    author='Dominik Lenoch',
    author_email='dlenoch@redhat.com'
)
