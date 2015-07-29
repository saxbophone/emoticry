#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


def load_tests(loader, tests, pattern):
    """
    Discover and load all unit tests in the test directory.
    This is the equivalent of running 'python -m unittest discover'
    from the command-line.
    """
    suite = unittest.TestSuite()
    # for all_test_suite in unittest.defaultTestLoader.discover():
    for all_test_suite in unittest.defaultTestLoader.discover('.'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    unittest.main()
