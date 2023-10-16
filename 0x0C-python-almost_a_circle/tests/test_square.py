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

    def test_size_prop_invalid_value(self):
        """
        checks if type error is raised with invalid value
        """
        s1 = Square(5)
        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_update_with_args(self):
        """
        tests if update with args work
        """
        s2 = Square(10, 20, 30, 40)

        s2.update(20)
        self.assertEqual(str(s2), "[Square] (20) 20/30 - 10")

        s2.update(5, 10)
        self.assertEqual(str(s2), "[Square] (5) 20/30 - 10")

        s2.update(100, 200, 300)
        self.assertEqual(str(s2), "[Square] (100) 300/30 - 200")

        s2.update(50, 60, 70, 80)
        self.assertEqual(str(s2), "[Square] (50) 70/80 - 60")

    def test_update_with_kwargs(self):
        """
        tests if the update works with kwargs
        """
        s2 = Square(10, 20, 30, 40)

        s2.update(x=50)
        self.assertEqual(str(s2), "[Square] (40) 50/30 - 10")

        s2.update(size=20, y=30)
        self.assertEqual(str(s2), "[Square] (40) 50/30 - 20")

        s2.update(size=100, id=200, y=300)
        self.assertEqual(str(s2), "[Square] (200) 50/300 - 100")

        s2.update(size=50, id=60, x=70, y=80)
        self.assertEqual(str(s2), "[Square] (60) 70/80 - 50")


if __name__ == '__main__':
    unittest.main()
