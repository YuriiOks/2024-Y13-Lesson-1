import unittest
from problem1_template import is_symmetrical

class TestProblem1(unittest.TestCase):

    def test_symmetrical_number(self):
        self.assertEqual(is_symmetrical(2002), 1)

    def test_non_symmetrical_number(self):
        self.assertNotEqual(is_symmetrical(1234), 1)

    def test_four_digit_symmetry(self):
        self.assertEqual(is_symmetrical(1221), 1)

    def test_padded_symmetry(self):
        self.assertEqual(is_symmetrical(21), 1)

    def test_padded_non_symmetry(self):
        self.assertNotEqual(is_symmetrical(210), 1)

if __name__ == '__main__':
    unittest.main()
