#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'c2c.recipe.closurecompile',
    version = '0.2.1',
    license = 'MIT License',

    author  = 'Frederic Junod',
    author_email = 'frederic.junod@camptocamp.com',
    url = 'https://github.com/camptocamp/c2c.recipe.closurecompile',

    description = 'A buildout recipe to compile javascript with the Google Closure Compiler',
    long_description = open('README.rst').read(),

    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
    ],

    zip_safe = False,
    install_requires = ['zc.buildout'],
    packages = find_packages(exclude=['ez_setup']),
    namespace_packages = ['c2c', 'c2c.recipe'],
    entry_points = {'zc.buildout' : ['default = c2c.recipe.closurecompile.buildout:ClosureCompile']}
)
