#!/usr/bin/python3
import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
"""
test cases for the class created in
the modelf folder
"""


class TestBase(unittest.TestCase):
    """
    class to run tests for the
    base class
    """
    def setUp(self):
        """
        setup function
        """
        pass

    def tearDown(self):
        """
        teardown function
        """
        pass

    """ def test_unique_ids(self):

        tets unique ids

        aq1 = Base()
        aw2 = Base()
        ae3 = Base()
        self.assertEqual(aq1.id, 1)
        self.assertEqual(aw2.id, 2)
        self.assertEqual(ae3.id, 3)
        """

    def test_given_id(self):
        """
        tests given ids
        """
        b = Base(12)
        self.assertEqual(b.id, 12)
        b = Base(42)
        self.assertEqual(b.id, 42)

    """ def test_no_given_id(self):

        test if no id were given

        bs = Base()
        self.assertEqual(bs.id, 1)
        """

    def test_neg_id(self):
        """
        test id for negatives
        """
        b = Base(-1)
        self.assertEqual(b.id, -1)
        b5 = Base(-102)
        self.assertEqual(b5.id, -102)

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

    def test_None_id(self):
        """
        tests with None as id
        """
        bd = Base()
        bd2 = Base(None)
        self.assertEqual(bd.id, 1)
        self.assertEqual(bd2.id, 2)

    def test_ids_acrross_instances(self):
        """
        test ids that ae accross instances
        """
        ba1 = Base()
        ba2 = Base()
        ba3 = Base()
        self.assertNotEqual(ba1.id, ba2.id)
        self.assertNotEqual(ba2.id, ba3.id)
        self.assertNotEqual(ba1.id, ba3.id)

    def test_to_json_string(self):
        """
        tests to see if json rep is correct
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        expected_json = json.dumps([dictionary])
        self.assertEqual(json_dict, expected_json)

    def test_save_to_file(self):
        """
        tests save to file fucntion
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            cont = file.read()
            expect = json.dumps([r1.to_dictionary(),
                                 r2.to_dictionary()])
            self.assertEqual(cont, expect)

        os.remove("Rectangle.json")


if __name__ == '__main__':
    unittest.main()
