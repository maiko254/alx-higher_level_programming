#!/usr/bin/python3
""" tests for class Base """
import unittest
from models.base import Base

class Test_Base(unittest.TestCase):
    """  Implements tests for Base object """

    def setUp(self):
        """ Creates instances of Base object """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(10)

    def test_ins_type(self):
        """ Tests that instance created is a Base instance """
        self.assertIsInstance(self.b1, Base)

    def test_has_attr(self):
        """ Test that instance of Base has attribute id """
        self.assertEqual(hasattr(self.b1, 'id'), True)

    def test_attr_id_None(self):
        """ Test id attribute increments only when id is None """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 10)
