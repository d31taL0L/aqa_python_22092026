numbers_list = [-4, 6, 3, 8, 5, 4, 0, 10, 17, 0]

even_numbers: list[int] = [number for number in numbers_list if number % 2 == 0]
print(sum(even_numbers))