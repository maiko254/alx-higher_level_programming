#!/usr/bin/python3
""" Test module for function max_integer """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class for function max_integer test cases """
    def test_none(self):
        """ Test empty list returns None """
        li = []
        self.assertIsNone(max_integer(li))

    def test_max_value(self):
        """ Test value returned is maximum """
        li = [2, 3, 23]
        self.assertEqual(max_integer(li), 23)

    def test_one_value(self):
        """ Test list with one value """
        li = [7]
        self.assertEqual(max_integer(li), 7)

    def test_type_str(self):
        li = [1, 2, '4']
        self.assertRaises(TypeError, max_integer, li)

    def test_type_float(self):
        li = [1, 3.0, 5]
        self.assertRaises(TypeError, max_integer(li))

    def test_is_list(self):
        li = [1, 2, 3]
        self.assertIsInstance(li, list)

    def test_args(self):
        li = [2, 3, 4]
        self.assertRaises(TypeError, max_integer, li, 2)

    def test_no_args(self):
        self.assertEqual(max_integer(), None)
