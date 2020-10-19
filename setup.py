# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 22:31:08 2020

@author: sriva
"""

"""Setup script for simpletext"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname("textslack"))
print(HERE)
# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="textslack",
    version="0.1.2",
    description="Play with text data",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AnkitRajSri/textslack.git",
    author="Ankit Raj",
    author_email="srivastavaankit667@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=["textslack"],
    include_package_data=True,
    install_requires=[
       "pandas", "nltk", "textblob", "sklearn", "normalise"
    ]
)