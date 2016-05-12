# -*- coding: utf-8 -*-

import re
from setuptools import setup

requires = [
    'requests>=2.0.0,<3.0.0'
]

setup(
    name = "python-nomad",
    long_description=(
        '%s\n\n%s' % (
            open('README.md').read(),
            open('CHANGELOG.md').read()
        )
    ),
    packages=["nomad",
              "nomad.api"],
    version=open('VERSION').read().strip(),
    description = "API for interacting with hashicorp nomad",
    author = "Gregory Durham",
    author_email = "gregory.durham@gmail.com",
    include_package_data=True,
    install_requires=requires
    )
