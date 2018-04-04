'''Setup file for a python template command-line program'''
from setuptools import setup, find_packages


with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

setup(
    name='python-cli-template',
    version='0.1.0',
    description='A template python program with a command-line interface.',
    long_description=README,
    author='Eugene Kovalev',
    author_email='eugene@kovalev.systems',
    url='https://github.com/Abraxos/python-cli-template',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={'console_scripts': ['python-cli-template=python_cli_template.core:main']},
    install_requires=REQUIREMENTS,
)
