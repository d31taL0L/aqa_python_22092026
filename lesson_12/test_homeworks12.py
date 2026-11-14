import unittest
from homeworks import sum_numbers_in_string, has_more_than_10_unique_chars, sum_even_numbers, filter_strings

class TestSumNumbersInString(unittest.TestCase):
    def test_valid_numbers_return_sum(self):
        result = sum_numbers_in_string("1,2,3,4")
        self.assertEqual(result, 10)

    def test_letters_return_error_message(self):
        result = sum_numbers_in_string("qwerty1,2,3")
        self.assertEqual(result, "I can't do that!")

    def test_empty_string_return_error_message(self):
        result = sum_numbers_in_string("")
        self.assertEqual(result, "I can't do that!")

class TestHasMore10UniqueChars(unittest.TestCase):
    def test_11_different_chars_return_true(self):
        result = has_more_than_10_unique_chars("abcdefghijk")
        self.assertTrue(result)

    def test_10_different_chars_return_false(self):
        result = has_more_than_10_unique_chars("abcdefghij")
        self.assertFalse(result)

    def test_long_string_of_identical_chars_return_false(self):
        result = has_more_than_10_unique_chars("aaaaaaaaaaaa")
        self.assertFalse(result)

class TestSumEvenNumbers(unittest.TestCase):
    def test_regular_list_return_sum(self):
        result = sum_even_numbers([-4, 6, 3, 8, 5, 4, 0, 10, 17, 0])
        self.assertEqual(result, 24)

    def test_empty_list_return_0(self):
        result = sum_even_numbers([])
        self.assertEqual(result, 0)

    def test_odd_numbers_list_return_0(self):
        result = sum_even_numbers([1, 3, 5])
        self.assertEqual(result, 0)

    def test_negative_even_numbers_list_return_negative_number(self):
        result = sum_even_numbers([-2, -4])
        self.assertEqual(result, -6)

class TestFilterStrings(unittest.TestCase):
    def test_mixed_list_return_only_strings(self):
        result = filter_strings(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', '', None, 3.14
                                    , ['a']])
        self.assertEqual(result, ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum', ''])

    def test_empty_list_return_empty_list(self):
        result = filter_strings([])
        self.assertEqual(result, [])

    def test_list_without_strings_return_empty_list(self):
        result = filter_strings([1, True, None])
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()