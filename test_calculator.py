import unittest
import calculator


# create unittests to test math functions in calculator.py
class TestCalculator(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(4, calculator.add(2, 2))

    def test_subtract(self):
        self.assertEqual(8, calculator.subtract(10, 2))

    def test_multiply(self):
        self.assertEqual(20, calculator.multiply(5, 4))

    def test_divide(self):
        self.assertEqual(6, calculator.divide(30, 5))


if __name__ == '__main__':
    unittest.main()
