import unittest
from AT01 import remainder

class TestDivide(unittest.TestCase):
    def test_remainder_success(self):
        self.assertEqual(remainder(10, 2), 0)
        self.assertEqual(remainder(23, 5), 3)
        self.assertEqual(remainder(17, -3), -1)
        self.assertEqual(remainder(-9, 2), 1)


    def test_remainder_by_zero(self):
        self.assertRaises(ValueError, remainder, 7, 0)
        self.assertRaises(ValueError, remainder, -11, 0)


    if __name__ == '__main__':
        unittest.main()