import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(3,2),5)
        self.assertNotEqual(Calculator.add(3,2),3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(7,2),5)
        self.assertNotEqual(Calculator.subtract(7,2),3)

    def test_multiply(self):
        self.assertNotEqual(Calculator.multiply(3,2),5)
        self.assertEqual(Calculator.multiply(3,2),6)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10,2),5)
        self.assertNotEqual(Calculator.divide(10,2),3)

if __name__ == '__main__':
    unittest.main()