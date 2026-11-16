import unittest
from homeworks import sum_even_numbers

class TestSumEvenNumbersPositive(unittest.TestCase):
    def test_regular_list_return_sum(self):
        result = sum_even_numbers([-4, 6, 3, 8, 5, 4, 0, 10, 17, 0])
        self.assertEqual(result, 24)

    def test_negative_even_numbers_list_return_negative_number(self):
        result = sum_even_numbers([-2, -4])
        self.assertEqual(result, -6)

class TestSumEvenNumbersNegative(unittest.TestCase):
    def test_empty_list_return_0(self):
        result = sum_even_numbers([])
        self.assertEqual(result, 0)

    def test_odd_numbers_list_return_0(self):
        result = sum_even_numbers([1, 3, 5])
        self.assertEqual(result, 0)