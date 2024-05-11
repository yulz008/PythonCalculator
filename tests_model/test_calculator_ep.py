import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_equivalence_partitions(self):
        # Test equivalence partitions for addition (valid, invalid)
        # Valid partition: any integer
        self.assertEqual(self.calc.add(5, 3), 8)  # Valid input
        # Invalid partition: non-integer or invalid input
        with self.assertRaises(TypeError):  # Example of an invalid input
            self.calc.add("hello", 3)

if __name__ == "__main__":
    unittest.main()