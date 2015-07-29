# emoticry

Mercilessly translates all names of files within a directory to emoji

[![Build Status](https://travis-ci.org/saxbophone/emoticry.svg?branch=develop)](https://travis-ci.org/saxbophone/emoticry)

```
usage: emoticry [-h] [-R] [-r] [path]

Mercilessly translates file names to emoji

positional arguments:
  path             Specifies the path to the directory where files and
                   directories will be renamed. (If not given then defaults to
                   the current directory).

optional arguments:
  -h, --help       show this help message and exit
  -R, --recursive  Recursively rename all files and directories.
  -r, --rescue     Restore the names of files and directories from emoji (Not
                   guaranteed to work between versions).

Please use this program with caution as recovery of file names is not
guaranteed!
```
