import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
from models.base import Base
"""
test nmodule to test the class Rectangle
"""


class TestRectangle(unittest.TestCase):
    """
    Test for the rectangle
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_constructor(self):
        """
        tests constructor
        """
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)

    def test_getters_setters(self):
        """
        test the getters and setters
        """
        r1 = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 30)
        self.assertEqual(r1.y, 40)

        r1.width = 100
        r1.height = 200
        r1.x = 300
        r1.y = 400
        self.assertEqual(r1.width, 100)
        self.assertEqual(r1.height, 200)
        self.assertEqual(r1.x, 300)
        self.assertEqual(r1.y, 400)

    def test_validation(self):
        """
        tests validations
        """
        with self.assertRaises(TypeError):
            r = Rectangle("10", 20, 30, 40, 50)
        with self.assertRaises(TypeError):
            r = Rectangle(10, "20", 30, 40, 50)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, "30", 40, 50)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, 30, "40", 50)
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20, 30, 40, 50)
        with self.assertRaises(ValueError):
            r = Rectangle(10, -20, 30, 40, 50)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -30, 40, 50)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 30, -40, 50)

    def test_area(self):
        """
        test the area method
        """
        res1 = Rectangle(5, 5)
        res2 = Rectangle(7, 3, 1, 2)
        res3 = Rectangle(3, 8, 0, 0, 0)
        self.assertEqual(res1.area(), 25)
        self.assertEqual(res2.area(), 21)
        self.assertEqual(res3.area(), 24)

    def test_display(self):
        """
        test the didsplay
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r1 = Rectangle(4, 6, 2, 1)
            r1.display()
            expected_output = '\n  ####\n'\
                              '  ####\n  ####\n  ####\n  ####\n  ####\n'
            self.assertEqual(mock_stdout.getvalue(), expected_output)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r2 = Rectangle(2, 2, 1, 0)
            r2.display()
            expected_output = ' ##\n ##\n'
            self.assertEqual(mock_stdout.getvalue(), expected_output)
    def test_str(self):
        """
        tests the str to print the rectangle info
        """
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(str(r), "[Rectangle] (50) 30/40 - 10/20")

        r = Rectangle(2, 10, 5)
        self.assertEqual(str(r), "[Rectangle] (1) 5/0 - 2/10")


if __name__ == '__main__':
    unittest.main()
