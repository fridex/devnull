#!/usr/bin/env python3
# This is just a joke. Why so serious...

from pathlib import Path

home = str(Path.home())
print(f"Removing directory {home!r} and setting the default runlevel to 0")
