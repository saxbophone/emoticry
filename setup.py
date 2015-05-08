#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from setuptools import setup


setup(
    name='emoticry',
    version='0.0.6',
    description='Mercilessly translates file names to emoji',
    long_description=('Mercilessly translates all names of files within a '
                      'directory to emoji. Please use this program with '
                      'caution as recovery of file names is not guaranteed!'),
    url='https://github.com/saxbophone/emoticry',
    author='Joshua Saxby',
    author_email='joshua.a.saxby@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: System Administrators',
        'Topic :: Artistic Software',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='emoji files hack deface joke',
    packages=['emoticry'],
    install_requires=[],
    extras_require={
        # 'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    package_data={
        '': ['README.md', 'LICENSE'],
    },
    entry_points={
        'console_scripts': [
            'emoticry=emoticry.main:main',
        ],
    },
    zip_safe=False,
)
