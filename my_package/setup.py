# my_package/setup.py
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'print-cctbx-version=my_package:print_cctbx_version',
        ],
    },
)
