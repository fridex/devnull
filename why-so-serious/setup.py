#!/usr/bin/env python3

from setuptools import setup
from setuptools.command.install import install


setup(
    name='why-so-serious',
    version='0.0.1',
    py_modules=["script"],
    dependency_links=[
        "git+https://github.com/fridex/devnull#subdirectory=pyjoker",
    ],
)
