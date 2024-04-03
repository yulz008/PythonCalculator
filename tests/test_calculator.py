"""Unit Tests"""

import unittest
import os
import sys
# Import the calculator module from the app package
from app.calculator import Calculator

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory of the current directory to the Python path
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)


# Unit tests for the Calculator class
class TestCalculator(unittest.TestCase):
    """Test Calculator Class"""
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        """Test addition module"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test subtraction module"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        """Test multiplication module"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """Test division module"""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_by_zero(self):
        """Test Divide by Zero"""
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)

if __name__ == "__main__":
    unittest.main()
