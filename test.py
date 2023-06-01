#!/usr/bin/env python

import pybel

import unittest

class TestErrors(unittest.TestCase):

    def test_hexagon_errors(self):
        with self.assertRaises(ValueError):
            pybel.getbook('', 1, 1, 1)

    def test_wall_errors(self):
        for num in (-1, 0, 5):
            with self.assertRaises(ValueError):
                pybel.getbook('a', num, 1, 1)

    def test_shelf_errors(self):
        for num in (-1, 0, 6):
            with self.assertRaises(ValueError):
                pybel.getbook('a', 1, num, 1)

    def test_volume_errors(self):
        for num in (-1, 0, 33):
            with self.assertRaises(ValueError):
                pybel.getbook('a', 1, 1, num)

if __name__ == "__main__":
    unittest.main()

