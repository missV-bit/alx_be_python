import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (1.5, 2.5, 4.0),
            (-2.5, -2.5, -5.0),
            (10**6, 10**6, 2 * 10**6),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)

    def test_subtraction(self):
        cases = [
            (5, 3, 2),
            (3, 5, -2),
            (0, 0, 0),
            (2.5, 1.0, 1.5),
            (-1, -1, 0),
            (10**6, 1, 10**6 - 1),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_multiplication(self):
        cases = [
            (3, 4, 12),
            (0, 100, 0),
            (-2, 3, -6),
            (2.5, 4, 10.0),
            (-2.5, -2.5, 6.25),
            (10**3, 10**3, 10**6),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_division_normal(self):
        cases = [
            (10, 2, 5.0),
            (3, 2, 1.5),
            (-6, 3, -2.0),
            (2.5, 0.5, 5.0),
            (10**6, 2, 5 * 10**5),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(self.calc.divide(a, b), expected, places=9)

    def test_division_by_zero_returns_none(self):
        cases = [
            (1, 0),
            (0, 0),
            (-5, 0),
        ]
        for a, b in cases:
            with self.subTest(a=a, b=b):
                self.assertIsNone(self.calc.divide(a, b))

    def test_division_with_non_integer_results(self):
        self.assertAlmostEqual(self.calc.divide(7, 3), 7/3, places=9)
        self.assertAlmostEqual(self.calc.divide(-7, 3), -7/3, places=9)

if __name__ == "__main__":
    unittest.main()
