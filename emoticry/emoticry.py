#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

"""emoticry.emoticry

This file contains the bulk of logic for the emoticry library.
"""


class Translation(object):
    """
    A generic Translation class for translating filenames.
    """
    def __init__(self, table=[hex(_)[2:] for _ in range(256)]):
        self.table = table

    def translate(self, name):
        new_name = ''
        for c in name:
            if len(c) == 1:
                new_name += self.table[ord(c)]
            else:
                new_name += c
        return new_name

 
def emojify(directory='.', recursive=False, translation=Translation()):
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
        for f in os.listdir(directory):
            os.rename(os.path.join(directory, f), os.path.join(directory, translation.translate(f)))
