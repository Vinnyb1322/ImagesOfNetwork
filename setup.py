#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = "images_of",
    version = "0.1.0",

    author = "acimi-ursi",
    description = "Tools for managing the ImagesOfNetwork on reddit",
    url = "https://github.com/amici-ursi/ImagesOfNetwork",

    packages = find_packages(),

    install_requires = [
        "click",
        "praw==3.4",
    ],

    entry_points = {
        "console_scripts": [
            "ion_expand = images_of.entrypoints.expand:main",
            "ion_setup_oauth = images_of.entrypoints.oauth:main",
            "ion_bot = images_of.entrypoints.bot:main",
        ],
    },
)
