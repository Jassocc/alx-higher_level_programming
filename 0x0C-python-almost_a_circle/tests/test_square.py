import unittest
from models.square import Square
"""
test casses for the class Square
"""


class TestSquare(unittest.TestCase):
    """
    class that contains test cases
    """
    def test_init(self):
        """
        test initializer
        """
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_str(self):
        """
        tests the string rep
        """
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_size_property(self):
        """
        tests the size property making sure
        it assigns both height and width to
        the same value
        """
        s = Square(7)
        self.assertEqual(s.size, 7)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_set_size(self):
        """
        tests to see if size sets correctly
        """
        s = Square(5)
        s.size = 8
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)


if __name__ == '__main__':
    unittest.main()
