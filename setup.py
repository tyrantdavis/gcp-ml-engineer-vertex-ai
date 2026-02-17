# setup.py
# This is required for python-package-uris
from setuptools import find_packages, setup

setup(
    name="course9_trainer",  # adjust the name if needed
    version="0.1.0",
    packages=find_packages(
        where="training"
    ),  # your trainer package is under training/trainer
    package_dir={"": "training"},  # base dir for packages
    install_requires=[
        "tensorflow>=2.13",
        "numpy",
        # Add other runtime dependencies here, e.g. pandas, numpy
    ],
    python_requires=">=3.8",
)
