#!/usr/bin/python3

"""
Has the test for the base module.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
# Base = __import__("models.base").base.Base
# Rectangle = __import__("models.rectangle").rectangle.Rectangle


class TestBase(unittest.TestCase):
    """Tests the Base class."""
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(12)
        self.b3 = Base("Hello")
        self.b4 = Base()
        self.b5 = Base(True)
        self.b6 = Base(1)
        self.b7 = Base(0)
        self.b8 = Base(-1)

    def test_id(self):
        """Tests the public instance attribute id."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 12)
        self.assertEqual(self.b3.id, "Hello")
        self.assertEqual(self.b4.id, 2)
        self.assertEqual(self.b5.id, True)
        self.assertEqual(self.b6.id, 1)
        self.assertEqual(self.b7.id, 0)
        self.assertEqual(self.b8.id, -1)
