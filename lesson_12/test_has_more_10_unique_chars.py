import unittest
from homeworks import has_more_than_10_unique_chars

class TestHasMoreThan10UniqueCharsPositive(unittest.TestCase):
    def test_11_different_chars_return_true(self):
        result = has_more_than_10_unique_chars("abcdefghijk")
        self.assertTrue(result)

class TestHasMoreThan10UniqueCharsNegative(unittest.TestCase):
    def test_10_different_chars_return_false(self):
        result = has_more_than_10_unique_chars("abcdefghij")
        self.assertFalse(result)

    def test_long_string_of_identical_chars_return_false(self):
        result = has_more_than_10_unique_chars("aaaaaaaaaaaa")
        self.assertFalse(result)