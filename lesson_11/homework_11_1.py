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

lst_of_values = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
for value in lst_of_values:
    print(sum_numbers_in_string(value))

print(sum_numbers_in_string(""))