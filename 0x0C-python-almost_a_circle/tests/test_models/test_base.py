#!/usr/bin/python3

"""This module contains unittests for base.py module."""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Testcases for id"""
    def test_id(self):
        b1 = Base()
        b2 = Base()
        
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

if __name__ == '__main__':
    unittest.main()
