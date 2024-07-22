#!/usr/bin/python3
"""Unittest for max_integer([...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_all(self):
        """Test for all positive with max in begining, middle and end"""
        self.assertEqual (max_integer([-45, -67, -12]), -12)
        self.assertEqual (max_integer([-81, -22, -92]), -22)
        self.assertEqual (max_integer([-100, -97, -35]), -35)
    def test_max(self):
        self.assertEqual(max_integer([10, 0, 2]), 10)
        self.assertEqual(max_integer([-3, 2, 55]), 55)
    def test_none(self):
        """Test for empty list []"""
        self.assertEqual(max_integer([]), None)
    def test_no_argument(self):
        """Test for no argument"""
        self.assertIsNone(max_integer())
    def test_none(self):
        """Test for None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)
    def test_wrong_type(self):
        """Test for wrong data type"""
        string = [1,2,"Wrong"]
        with self.assertRaises(TypeError):
            max_integer(string)
            
if __name__ == '__main__':
    unittest.main()
