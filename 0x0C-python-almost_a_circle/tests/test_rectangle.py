import unittest
from models.rectangle import Rectangle
"""
test nmodule to test the class Rectangle
"""


class TestRectangle(unittest.TestCase):
    """
    Test for the rectangle
    """
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


if __name__ == '__main__':
    unittest.main()
