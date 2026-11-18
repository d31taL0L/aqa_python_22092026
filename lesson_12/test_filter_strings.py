import unittest
from homeworks import filter_strings

class TestFilterStringsPositive(unittest.TestCase):
    def test_mixed_list_return_only_strings(self):
        result = filter_strings(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', '', None, 3.14
                                    , ['a']])
        self.assertEqual(result, ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum', ''])

class TestFilterStringsNegative(unittest.TestCase):
    def test_empty_list_return_empty_list(self):
        result = filter_strings([])
        self.assertEqual(result, [])

    def test_list_without_strings_return_empty_list(self):
        result = filter_strings([1, True, None])
        self.assertEqual(result, [])