#!/usr/bin/env python

import os
from setuptools import setup

setup(
    name = 'CITS3403 Project',
    version = '1.0',
    install_requires = [
        'flask',
        'flask-wtf',
        'Flask-SQLAlchemy',
        'mysql-connector-python',
        'pymysql',
        'cryptography',
        'Flask-Migrate'
        'flask-login'
    ]
)