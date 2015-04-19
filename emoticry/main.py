#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

import emoticry

"""emoticry.main

This file provides the main entry point for using this library
as a command line program.
"""


def main():
    """
    The main entry point function for running emoticry from the command line.
    """
    parser = argparse.ArgumentParser(
        prog='Emoticry',
        description='Mercilessly translates file names to emoji',
        epilog=('This program must be used with extreme caution '
                'as there is currently no way to revert filenames!'))
    parser.add_argument('path', nargs='?', default='.')
    parser.add_argument('-R', dest='recursive', action='store_true')
    parser.set_defaults(recursive=False)
    args = parser.parse_args()
    emoticry.emojify(args.path, args.recursive)
