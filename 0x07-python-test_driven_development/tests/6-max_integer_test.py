#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    test case for max_integer
    """
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1.5, 1.3]), 1.5)
        self.assertEqual(max_integer([-1.5, -1.3]), -1.3)
    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 6, 2]), 6)
        self.assertEqual(max_integer([-2, -3, -6, -1]), -1)
        self.assertEqual(max_integer([10, 10, -10]), 10)
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer([None]), None)
        self.assertIsNone(max_integer(), None)
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -4, -7, -8]), -1)
    def test_float_nums(self):
        self.assertEqual(max_integer([1.7, 1.8, 2.5]), 2.5)
        self.assertEqual(max_integer([-1.4, -2.8, -3.2]), -1.4)
    def test_strings(self):
        self.assertEqual(max_integer("6789"), '9')
        self.assertEqual(max_integer("54321"), '5')
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer("abcde"), 'e')
        self.assertEqual(max_integer("12 34 56"), '6')
        self.assertEqual(max_integer(['a', 'b', 'c', 'x', 'y']), 'y')
        self.assertEqual(max_integer(["abc", 'x']), 'x')
    def test_multiple_arguments(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2}, {3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer("12345", {6, 7, 8, 9})
        with self.assertRaises(TypeError):
            max_integer("12345", {'a': 1, 'b': 2})
    def test_invalid_list_element(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3"])
    def test_invalid_argument_type(self):
        with self.assertRaises(TypeError):
            max_integer(123)
        with self.assertRaises(TypeError):
            max_integer([True, None])
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer([None, True])
        with self.assertRaises(TypeError):
            max_integer(-10, 0.5, "str", {1, 2})
    def test_module_doc(self):
        moduleDocstring = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDocstring) > 1)
    def test_function_doc(self):
        funcDocstring = __import__('6-max_integer').__doc__
        self.assertTrue(len(funcDocstring) > 1)
if __name__ == "__main__":
    unittest.main()
