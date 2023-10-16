#!/usr/bin/python3
"""
test cases for the class created in
the modelf folder
"""
import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


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

    def test_from_json_empty_string(self):
        """
        tests empty json string
        """
        json_string = ""
        res = Rectangle.from_json_string(json_string)
        self.assertEqual(res, [])

    def test_from_json_string_none(self):
        """
        tests None jsonm string
        """
        json_string = None
        res = Rectangle.from_json_string(json_string)
        self.assertEqual(res, [])

    def test_from_json_string_valid(self):
        """
        tests json string with valid value
        """
        json_string = '[{"id": 89, "width": 10, "height": 4}, \
                {"id": 7, "width": 1, "height": 7}]'
        res = Rectangle.from_json_string(json_string)
        expected = [{'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}]
        self.assertEqual(res, expected)

    def test_create_rectangle(self):
        """
        tests the create ffunction
        """
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertIsNot(r1, r2)

    def test_load_from_file(self):
        """
        tests loading instances from file)
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        for rect_input, rect_output in zip(
                list_rectangles_input, list_rectangles_output):
            self.assertEqual(rect_input.id, rect_output.id)
            self.assertEqual(rect_input.width, rect_output.width)
            self.assertEqual(rect_input.height, rect_output.height)
            self.assertEqual(rect_input.x, rect_output.x)
            self.assertEqual(rect_input.y, rect_output.y)


if __name__ == '__main__':
    unittest.main()
