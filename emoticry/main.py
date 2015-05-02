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
        epilog=('Please use this program with caution as '
                'recovery of file names is not guaranteed!'))

    parser.add_argument('path',
                        nargs='?',
                        default='.',
                        help=('Specifies the path to the directory where '
                              'files and directories will be renamed. '
                              '\n(If not given then defaults to the current '
                              'directory).'))

    parser.add_argument('-R',
                        '--recursive',
                        dest='recursive',
                        action='store_true',
                        help=('Recursively rename all files and directories.'))

    parser.add_argument('-r',
                        '--rescue',
                        dest='rescue',
                        action='store_true',
                        help=('Restore the names of files and directories '
                              'from emoji (Not guaranteed to work between '
                              'versions).'))

    parser.set_defaults(recursive=False,
                        rescue=False)

    args = parser.parse_args()

    emoticry.emojify(directory=unicode(args.path, 'utf-8'),
                     recursive=args.recursive,
                     rescue=args.rescue)
