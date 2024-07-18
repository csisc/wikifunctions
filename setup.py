# setup.py

from setuptools import setup, find_packages

setup(
    name="wikifunctions",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Houcemeddine Turki",
    author_email="turkiabdelwaheb@hotmail.fr",
    description="A package to load and reuse Wikifunctions implementations.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/csisc/wikifunctions",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
