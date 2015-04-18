#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

"""emoticry.emoticry

This file contains the bulk of logic for the emoticry library.
"""


def emojify(directory='.', recursive=False):
    """
    For the given directory, iterate over all files and folders within it
    (optionally recursively) and translate the file name characters to emoji.
    """
    if recursive:
        for files in os.walk(directory, topdown=True):
            path = files[0]
            directories = files[1]
            filenames = files[2]
            print('Directories in {0}:'.format(path))
            for d in directories:
                print(d)
            for f in filenames:
                print(f)
    else:
        for files in os.listdir(directory):
            print(files)
