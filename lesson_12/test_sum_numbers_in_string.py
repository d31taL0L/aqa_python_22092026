import unittest
from homeworks import sum_numbers_in_string

class TestSumNumbersInStringPositive(unittest.TestCase):
    def test_valid_numbers_return_sum(self):
        result = sum_numbers_in_string("1,2,3,4")
        self.assertEqual(result, 10)

class TestSumNumbersInStringNegative(unittest.TestCase):
    def test_letters_return_error_message(self):
        result = sum_numbers_in_string("qwerty1,2,3")
        self.assertEqual(result, "I can't do that!")


    def test_empty_string_return_error_message(self):
        result = sum_numbers_in_string("")
        self.assertEqual(result, "I can't do that!")