while True:
    input_str = input("Enter a word that contains the letter 'h' (upper or lower case): ")
    input_str_lower = input_str.lower()
    if 'h' in input_str_lower:
        print(input_str)
        print("Program stopped")
        break
    else:
        print(input_str)
        print()
