from pathlib import Path

from setuptools import find_packages, setup

long_description = Path("README.md").read_text()
required = Path("requirements.txt").read_text().splitlines()


setup(
    name="raffaelo",
    version="0.0.2",
    author="e183b796621afbf902067460",
    author_email="606d18446a06fe9738fd@gmail.com",
    url="https://github.com/e183b796621afbf902067460/raffaelo",
    packages=find_packages(),
    long_description=long_description,
    install_requires=required,
)
