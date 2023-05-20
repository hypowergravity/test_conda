# my_package/my_package/main.py
from __future__ import absolute_import, division, print_function
import cctbx

def print_cctbx_version():
    print(f'CCTBX version: {cctbx.__version__}')
