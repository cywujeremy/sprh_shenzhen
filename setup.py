# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

setup(
    name='sprh',
    version='0.0.1',
    description='a data analysis project realized using Python',
    long_description=readme,
    author='Chengyu Wu',
    author_email='chengyu2@andrew.cmu.edu',
    url='https://github.com/cywujeremy/sprh_shenzhen',
    #license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)