# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from typing import Any


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

print()
# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(first_number, second_number):
    result = f"Результат: {int(first_number) + int(second_number)}"
    return result

print(sum_numbers(3, 4))
print(sum_numbers(-5, 5))
print(sum_numbers(0.1, 0.2))
print(sum_numbers('3', '4'))

print()
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avg_result(lst):
    if len(lst) == 0:
        return None
    else:
        sum_result = 0
        for number in lst:
            sum_result += number

        average = sum_result / len(lst)
        return average

print(avg_result([1, 2, 3, 4]))
print(avg_result([]))
print(avg_result([7]))
print(avg_result([-4, 4]))
print(avg_result([0.1, 0.2]))

print()
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_text(text):
    return text[::-1]

print(reverse_text("string"))
print(reverse_text(""))
print(reverse_text("a"))
print(reverse_text("level"))
print(reverse_text("Hello, World!"))

print()
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(list_of_words):
    l_word = ''
    if len(list_of_words) == 0:
        return None
    for word in list_of_words:
        if len(word) > len(l_word):
            l_word = word
    return l_word

words = ['integer', 'qwerty12345', 'hi']
empty_list = []
same_words = ['cat', 'dog']
result1 = longest_word(words)
result2 = longest_word(empty_list)
result3 = longest_word(same_words)
print(result1)
print(result2)
print(result3)

print()
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    full_text = str1
    find_the_word = str2
    position_index = full_text.find(find_the_word)

    return position_index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

print()
# task 7
def calculate_fuel_and_refuels(distance_km, fuel_per_100km, tank_capacity, start_with_full_tank=True):
    """
    The function calculates how many liters of gasoline will be needed for a trip and how many times you'll need
    to stop at a gas station to fill up the tank.

    Args:
        distance_km: The distance of the trip itself (km)
        fuel_per_100km: Fuel consumption per 100 km (liters)
        tank_capacity: Car Fuel Tank Capacity (liters)
        start_with_full_tank: If the value is True, the tank is completely full; If set to False, the tank is empty at
        the start, so each tank is filled at the gas station.

    Returns:
        Returns the number of liters needed for the trip and how many times you'll need to stop at a gas station
        (tuple[float, int])
    """
    fuel_liters = (distance_km / 100) * fuel_per_100km
    refills_needed = fuel_liters // tank_capacity
    extra_liters = fuel_liters % tank_capacity

    if extra_liters > 0:
        refills_needed += 1

    if start_with_full_tank and refills_needed > 0:
        refills_needed -= 1

    return fuel_liters, int(refills_needed)

task1 = calculate_fuel_and_refuels(1600, 9, 48)
task2 = calculate_fuel_and_refuels(1650, 9, 48)
task3 = calculate_fuel_and_refuels(0, 9, 48)
task4 = calculate_fuel_and_refuels(300, 9, 48)
task5 = calculate_fuel_and_refuels(1600, 9, 48, False)
print(task1)
print(task2)
print(task3)
print(task4)
print(task5)

print()
# task 8

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

print(has_more_than_10_unique_chars('abcdefghij'))
print(has_more_than_10_unique_chars('abcdefghijk'))
print(has_more_than_10_unique_chars('aaaaaaaaaaaa'))

print()
# task 9
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

print(sum_even_numbers([-4, 6, 3, 8, 5, 4, 0, 10, 17, 0]))
print(sum_even_numbers([]))
print(sum_even_numbers([1, 3, 5]))
print(sum_even_numbers([-2, -4]))

print()
# task 10
def filter_strings(lst_of_data: list[Any]):
    """
    The purpose of this function is to filter the list and keep only data in string format.
    Args:
        lst_of_data: A list containing various types of data, for filtering (list[Any])
    Returns:
        Returns a list containing only strings. Empty list if there are no strings.
    """
    strings_only = [str_data
                    for str_data in lst_of_data
                    if isinstance(str_data, str)]

    return strings_only

print(filter_strings(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', '', None, 3.14, ['a']]))
print(filter_strings([]))
print(filter_strings([1, True, None]))
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""