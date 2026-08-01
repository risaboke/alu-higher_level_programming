#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Max is found in an already sorted ascending list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max is found in an unsorted list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_start(self):
        """Max is found when it is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_end(self):
        """Max is found when it is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Max is found when it is somewhere in the middle."""
        self.assertEqual(max_integer([1, 5, 2, 3]), 5)

    def test_single_element(self):
        """A single-element list returns that element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Calling with no argument uses the empty-list default."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Max is found among negative numbers."""
        self.assertEqual(max_integer([-1, -5, -2, -10]), -1)

    def test_mixed_positive_negative(self):
        """Max is found among a mix of positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 10, -20, 5]), 10)

    def test_all_equal_elements(self):
        """All elements equal returns that repeated value."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_two_equal_maxes(self):
        """The first occurrence of a tied max is returned."""
        self.assertEqual(max_integer([3, 9, 5, 9, 1]), 9)

    def test_float_values(self):
        """Max is found among floats."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_int_and_float(self):
        """Max is found among a mix of ints and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_does_not_mutate_input(self):
        """The original list is left unmodified."""
        original = [3, 1, 4, 1, 5]
        max_integer(original)
        self.assertEqual(original, [3, 1, 4, 1, 5])

    def test_return_type_is_not_a_list(self):
        """The function returns a single value, not a list."""
        self.assertNotIsInstance(max_integer([1, 2, 3]), list)


if __name__ == '__main__':
    unittest.main()
