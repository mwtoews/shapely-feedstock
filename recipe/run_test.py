"""Run test script for shapely."""
import platform
import py
import os
import sys

from shapely import speedups
from shapely.geometry import LineString


implementation = platform.python_implementation()
print(f'implementation: {implementation}')
target_platform = os.environ["target_platform"]
print(f'target platform: {target_platform}')
py_version = sys.version_info[:2]
print(f'python version: {py_version}')

pytest_args = ['tests']


if speedups.available and not speedups.enabled:
    speedups.enable()

print("speedups enabled: {speedups.enabled}")
if speedups.enabled:
    pytest_args.append('--with-speedups')
else:
    pytest_args.append('--without-speedups')

py.test.cmdline.main(pytest_args)

ls = LineString([(0, 0), (10, 0)])
# On OSX causes an abort trap, due to https://github.com/Toblerity/Shapely/issues/177
r = ls.wkt
area = ls.buffer(10).area

# Check if we can import lgeos.
# https://github.com/conda-forge/shapely-feedstock/issues/17
from shapely.geos import lgeos
