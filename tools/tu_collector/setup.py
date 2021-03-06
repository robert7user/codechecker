#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tu_collector",
    version="0.1.0",
    author='CodeChecker Team (Ericsson)',
    description="Collect the source files constituting a translation unit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ericsson/CodeChecker",
    keywords=['tu-collector', 'translation unit', 'collector',
              'compilation database'],
    license='LICENSE.txt',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: University of Illinois/NCSA Open Source License",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    entry_points={
        'console_scripts': [
            'tu-collector = tu_collector.tu_collector:main'
        ]
    },
)
