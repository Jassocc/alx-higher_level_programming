#!/usr/bin/python3
import unittest
from models.base import Base
import subprocess
"""
test cases for the class created in
the modelf folder
"""


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
        b = Base(12)
        self.assertEqual(b.id, 12)
        b = Base(42)
        self.assertEqual(b.id, 42)

    def test_no_given_id(self):
        """
        test if no id were given
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
    
    def test_neg_id(self):
        """
        test id for negatives
        """
        b = Base(-1)
        self.assertEqual(b.id, -1)
        b2 = Base(-102)
        self.assertEqual(b.id, -102)

    def test_large_id(self):
        """
        tests large ids
        """
        b = Base(99999)
        self.assertEqual(b.id, 99999)

    def test_string_id(self):
        """
        tests string ids
        """
        b = Base("abc")
        self.assertEqual(b.id, "abc")

    def test_float_id(self):
        """
        test float ids
        """
        b = Base(3.14)
        self.assertEqual(b.id, 3.14)

    def test_None_id(Self):
        """
        tests with None as id
        """
        b1 = Base()
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_ids_acrross_instances(self):
        """
        test ids that ae accross instances
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b3.id)
        self.assertNotEqual(b1.id, b3.id)

    def test_pep8_comp(self):
        """
        test if case is pep 8 compliant
        """
        file_to_check = 'models/base.py'
        res = subprocess.run(['flake8', file_to_check], stdout=subprocess.PIPE)
        self.assertEqual(res.returncode, 0, f"PEP 8 Violations found in {file_to_check}")

if __name__ == '__main__':
    unittest.main()
