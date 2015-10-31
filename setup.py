#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages

__version__ = "1.0.3"

setup (name = "braindocsclient",
        version = __version__,
        description = ("The braindocsclient facilitates communication between client and BrainDocs API"
                       " and collects client scripts for braindocs/analyst-toolbox."),
        packages = ["braindocsclient", "braindocs2database"],
        author="Thomas Diggelmann",
        author_email="td@ai-one.com",
        url="https://github.com/ai-one/braindocsClient",
        install_requires=["requests", "sqlalchemy", "python-dateutil"],
        entry_points={
            'console_scripts': [
                'braindocs2database = braindocs2database.__main__:main'
            ]
        })