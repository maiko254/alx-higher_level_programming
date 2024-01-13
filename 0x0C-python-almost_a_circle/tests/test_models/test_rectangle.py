#!/usr/bin/python3
""" Implements test class for Rectangle class """


from models.rectangle import Rectangle
from models.base import Base
import unittest


class Test_Rectangle(unittest.TestCase):
    """ creates test cases for a Rectangle object """

    def setUp(self):
        """ creates Rectangle objects for use in test cases """
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(4, 3, 2, 3)
        self.r3 = Rectangle(5, 2, 6, 7, 9)

    def test_instance_type(self):
        """ Test object instance is Rectangle """
        self.assertIsInstance(self.r1, Rectangle)

    def test_child_class(self):
        """ Test if Rectangle inherits Base class """
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_args(self):
        """ Test object created with different number of arguments """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.width, 4)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 3)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.width, 5)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 6)
        self.assertEqual(self.r3.y, 7)
        self.assertEqual(self.r3.id, 9)
