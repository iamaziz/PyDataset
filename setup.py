#!/usr/bin/env python

# Author: Aziz Alto
# email: iamaziz.alto@gmail.com

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='pydataset',
    description=("Provides instant access to many popular datasets right from "
                 "Python (in dataframe structure)."),
    author='Aziz Alto',
    url='https://github.com/iamaziz/PyDataset',
    download_url='https://github.com/iamaziz/PyDataset/tarball/0.2.0',
    license = 'MIT',
    author_email='iamaziz.alto@gmail.com',
    version='0.2.0',
    install_requires=['pandas'],
    packages=['pydataset', 'pydataset.utils'],
    package_data={'pydataset': ['*.gz', 'resources.tar.gz']}
)
