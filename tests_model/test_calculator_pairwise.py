import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_pairwise_testing(self):
        # Pairwise testing for addition
        # Test pairs of values that cover all possible combinations
        test_cases = [
            (0, 0),  # 0 + 0 = 0
            (1, 0),  # 1 + 0 = 1
            (0, 1),  # 0 + 1 = 1
            (-1, 0), # -1 + 0 = -1
            (0, -1), # 0 + (-1) = -1
            (10, 20),  # 10 + 20 = 30
            (-10, -20),  # -10 + (-20) = -30
        ]
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), a + b)

if __name__ == "__main__":
    unittest.main()
