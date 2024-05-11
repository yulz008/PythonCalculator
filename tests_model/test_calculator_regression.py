import unittest
from calculator import Calculator

# Unit tests for the Calculator class
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        # Basic addition tests
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(0, 0), 0)

        # Test adding large numbers
        self.assertEqual(self.calc.add(1000000, 1000000), 2000000)

    def test_subtract(self):
        # Basic subtraction tests
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertEqual(self.calc.subtract(0, 0), 0)

        # Test subtracting large numbers
        self.assertEqual(self.calc.subtract(1000000, 500000), 500000)

    def test_multiply(self):
        # Basic multiplication tests
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

        # Test multiplying by zero
        self.assertEqual(self.calc.multiply(1000000, 0), 0)

    def test_divide(self):
        # Basic division tests
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 5), 0)

        # Test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)

        # Test division with fractional result
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.3333, places=4)

    def test_regression(self):
        # Additional regression tests
        self.assertEqual(self.calc.add(2, -3), -1)  # Test negative numbers in addition
        self.assertEqual(self.calc.subtract(5, -3), 8)  # Test negative numbers in subtraction
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # Test negative numbers in multiplication
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=4)  # Test division with fractional result

if __name__ == "__main__":
    unittest.main()
