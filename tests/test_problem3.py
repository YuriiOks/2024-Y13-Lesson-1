import unittest
import re
from problem3_template import is_divisible_without_remainder

class TestProblem3(unittest.TestCase):

    def test_forbidden_constructs(self):
        with open('problem3_template.py', 'r') as file:
            content = file.read()
            self.assertIsNone(re.search(r'\b(if|for|while|def)\b', content), "Forbidden constructs used")

    def test_divisible_numbers(self):
        self.assertEqual(is_divisible_without_remainder(10, 5), 'YES')

    def test_non_divisible_numbers(self):
        self.assertEqual(is_divisible_without_remainder(9, 4), 'NO')

    def test_divisible_larger_numbers(self):
        self.assertEqual(is_divisible_without_remainder(100, 10), 'YES')

    def test_zero_division(self):
        self.assertEqual(is_divisible_without_remainder(0, 10), 'YES')

    def test_division_by_zero(self):
        # Assuming the function handles division by zero appropriately
        self.assertEqual(is_divisible_without_remainder(10, 0), 'NO')

if __name__ == '__main__':
    unittest.main()
