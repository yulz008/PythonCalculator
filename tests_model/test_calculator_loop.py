import unittest
from calculator import Calculator

# Unit tests for the Calculator class
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_all_possible_inputs(self):
        for a in range(-1000, 1001):  # Test integers from -100 to 100
            for b in range(-1000, 1001):
                result = self.calc.add(a, b)
                self.assertEqual(result, a + b)

    def test_subtract_all_possible_inputs(self):
        for a in range(-1000, 1001):  # Test integers from -100 to 100
            for b in range(-1000, 1001):
                result = self.calc.subtract(a, b)
                self.assertEqual(result, a - b)

    # Similar tests for multiply and divide, covering a range of inputs

if __name__ == "__main__":
    unittest.main()