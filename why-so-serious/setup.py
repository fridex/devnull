#!/usr/bin/env python3

from setuptools import setup


setup(
    name='why-so-serious',
    version='0.0.1',
    py_modules=["script"],
    install_requires=[
        "pyjoker @ git+https://github.com/fridex/devnull.git#subdirectory=pyjoker",
    ],
)
