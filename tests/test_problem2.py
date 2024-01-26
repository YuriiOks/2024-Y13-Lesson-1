import unittest
import re
from problem2_template import find_max_without_conditionals

class TestProblem2(unittest.TestCase):

    def test_forbidden_constructs(self):
        with open('problem2_template.py', 'r') as file:
            content = file.read()
            self.assertIsNone(re.search(r'\b(if|for|while|def)\b', content), "Forbidden constructs used")

    def test_both_numbers_equal(self):
        self.assertEqual(find_max_without_conditionals(100, 100), 100)

    def test_first_number_larger(self):
        self.assertEqual(find_max_without_conditionals(9, 3), 9)

    def test_second_number_larger(self):
        self.assertEqual(find_max_without_conditionals(4, 10), 10)

    def test_zero_values(self):
        self.assertEqual(find_max_without_conditionals(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
