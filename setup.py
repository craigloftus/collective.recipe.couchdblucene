# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

version = open(os.path.join("version.txt")).read().strip()

setup(
    name='collective.recipe.couchdblucene',
    version=version,
    description="zc.buildout to configure a couchdb-lucene instance",
    long_description=open(os.path.join("README.md")).read() + "#n" +
                     open(os.path.join("docs", "CHANGES.rst")).read() + "#n" +
                     open(os.path.join("docs", "CONTRIBUTORS.rst")).read(),
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='',
    author='Michael Davis',
    author_email='m.r.davis"me.com',
    url='http://pypi.python.org/pypi/collective.recipe.couchdblucene',
    license='ZPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'zc.buildout': ['default = collective.recipe.couchdblucene:Recipe']
    },
)

