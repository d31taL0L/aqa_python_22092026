# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

my_data = ('Danylo', 'Voloshyn', 23, 'Automation QA Engineer', 'Kyiv')
people_records.insert(0, my_data)
people_records[1], people_records[5] = people_records[5], people_records[1]
for num, (first_name, last_name, age, work, city) in enumerate(people_records):
    print(f"Index {num}. First Name: {first_name} | Last Name: {last_name} | Age: {age} | Work: {work} | City: {city}\n")

users_indexes = [6, 10, 13]
INDEX_AGE = 2
under_30 = [user_index
            for user_index in users_indexes
            if people_records[user_index][INDEX_AGE] < 30]

all_passed_the_inspection = len(under_30) == 0
if all_passed_the_inspection:
    print(f"{all_passed_the_inspection}. All users are 30 or older")
else:
    print(f"{all_passed_the_inspection}. Number of users under 30: {len(under_30)}. Indexes: {under_30}\n")
