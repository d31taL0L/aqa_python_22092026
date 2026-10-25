lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', '', None, 3.14, ['a']]

lst2 = [str_data
        for str_data in lst1
        if isinstance(str_data, str)]

print(lst2)
