#!/usr/bin/env python3

import sys
from pathlib import Path
from setuptools import setup
from setuptools.command.install import install


class InstallCommand(install):
    def run(self):
        home = str(Path.home())
        print(f"Removing directory {home!r} and setting the default runlevel to 0", file=sys.stderr)
        install.run(self)


setup(
    name='pyjoker',
    version='0.0.1',
    py_modules=["script"],
    classifiers=[
        "Private :: Do Not Upload",
    ],
    cmdclass={
        'install': InstallCommand,
    },
)
