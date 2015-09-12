#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages

__version__ = "1.0.0"

setup (name = "braindocs-client",
        version = __version__,
        description = "The braindocs-client collects client scripts to help with braindocs/analys-toolbox.",
        packages = ["braindocs2database"],
        author="Thomas Diggelmann",
        author_email="td@ai-one.com",
        url="https://github.com/ai-one/braindocsClient",
        install_requires=["requests", "sqlalchemy", "python-dateutil", "mysql-python"],
        entry_points={
            'console_scripts': [
                'braindocs2database = braindocs2database.__main__:main'
            ]
        })