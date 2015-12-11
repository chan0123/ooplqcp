#!/usr/bin/env python3

# -----------------
# RangeIteratorT.py
# -----------------

from unittest import main, TestCase

from RangeIterator import RangeIterator

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [RangeIterator]

    def test_1 (self) :
        for f in self.a :
                p = f(2, 2)
                self.assertIs(iter(p), p)
                self.assertRaises(StopIteration, next, p)

    def test_2 (self) :
        for f in self.a :
                p = f(2, 3)
                self.assertIs(iter(p), p)
                self.assertEqual(p.next(), 2)
                self.assertRaises(StopIteration, next, p)

    def test_3 (self) :
        for f in self.a :
                p = f(2, 4)
                self.assertIs(iter(p), p)
                self.assertEqual(p.next(), 2)
                self.assertEqual(p.next(), 3)
                self.assertRaises(StopIteration, next, p)

    def test_4 (self) :
        for f in self.a :
                p = f(2, 5)
                self.assertEqual(list(p), [2, 3, 4])
                self.assertEqual(list(p), [])

if __name__ == "__main__" :
    main()
