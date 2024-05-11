import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_boundary_values(self):
        # Test boundary values for addition (boundary - 1, boundary, boundary + 1)
        boundary = 1000
        self.assertEqual(self.calc.add(boundary - 1, 1), boundary)  # Just below boundary
        self.assertEqual(self.calc.add(boundary, 0), boundary)      # At boundary
        self.assertEqual(self.calc.add(boundary + 1, -1), boundary) # Just above boundary

   
if __name__ == "__main__":
    unittest.main()