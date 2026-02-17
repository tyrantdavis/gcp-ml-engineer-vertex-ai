# setup.py
# This is required for python-package-uris
%%writefile setup.py
from setuptools import setup, find_packages

setup(
    name="course9_trainer",
    version="0.1",
    packages=find_packages(),
)
