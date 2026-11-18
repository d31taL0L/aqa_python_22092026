from typing import Any


def sum_numbers_in_string(value):
    try:
        lst_of_numbers = value.split(",")
        sum_numbers = 0
        for number in lst_of_numbers:
            number_to_integer = int(number)
            sum_numbers += number_to_integer
        return sum_numbers
    except ValueError:
        return "I can't do that!"


def has_more_than_10_unique_chars(text):
    """
    The purpose of this function is to determine whether the text contains more than 10 unique characters.
    Args:
         text: The string in which we are counting the characters. (string)
    Returns:
         Returns a boolean value. True if the text contains more than 10 unique characters; False if it contains 10 or
         fewer unique characters. (bool)
    """

    return len(set(text)) > 10

def sum_even_numbers(lst_of_numbers: list[int]):
    """
    The purpose of this function is to sum even numbers.
    Args:
         lst_of_numbers: list of integers to sum the even ones from (list[int])
    Returns:
        The sum of even numbers (int)
    """

    even_numbers: list[int] = [number for number in lst_of_numbers if number % 2 == 0]

    return sum(even_numbers)

def filter_strings(lst_of_data: list[Any]):
    strings_only = [str_data
                    for str_data in lst_of_data
                    if isinstance(str_data, str)]

    return strings_only