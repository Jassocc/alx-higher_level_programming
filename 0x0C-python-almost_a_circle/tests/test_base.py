#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    class to run tests for the
    base class
    """
    def test_unique_ids(self):
        """
        tets unique ids
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_given_id(self):
        """
        tests given ids
        """

