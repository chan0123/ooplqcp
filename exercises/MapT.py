#!/usr/bin/env python3

# -------
# MapT.py
# -------

# https://docs.python.org/3.5/library/functions.html#map

from unittest import main, TestCase

from Map import    \
    map_range_for, \
    map_for,       \
    map_while_1,   \
    map_while_2,   \
    map_generator

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            map_range_for,
            map_for,
            map_while_1,
            map_while_2,
            map_generator,
            map]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(list(f(lambda x : x ** 2, ())), [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(list(f(lambda x : x ** 2, (2,))), [4])

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(list(f(lambda x : x ** 2, (2, 3))), [4, 9])

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(list(f(lambda x : x ** 2, (2, 3, 4))), [4, 9, 16])

if __name__ == "__main__" :
    main()

"""
% MapT
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
"""
