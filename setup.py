#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

from opps import hubcasts


install_requires = ["opps"]

classifiers = ["Development Status :: 4 - Beta",
               "Intended Audience :: Developers",
               "Operating System :: OS Independent",
               "Framework :: Django",
               'Programming Language :: Python',
               "Programming Language :: Python :: 2.7",
               "Operating System :: OS Independent",
               "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
               'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.md').read()
except:
    long_description = hubcasts.__description__

setup(name='opps-hubcasts',
      namespace_packages=['opps'],
      version=hubcasts.__version__,
      description=hubcasts.__description__,
      long_description=long_description,
      classifiers=classifiers,
      keywords='blogs blog multi-blog app opps cms',
      author=hubcasts.__author__,
      author_email=hubcasts.__email__,
      packages=find_packages(exclude=('doc', 'docs',)),
      install_requires=install_requires,
      include_package_data=True,)
