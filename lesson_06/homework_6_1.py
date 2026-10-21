unique_char = set()

string = input()
for char in string:
    unique_char.add(char)

result = len(unique_char) > 10
print(f"Result: {result}")
