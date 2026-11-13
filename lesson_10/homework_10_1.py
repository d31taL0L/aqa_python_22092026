from abc import ABC, abstractmethod
import math


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
        def __init__(self, department, **kwargs):
            super().__init__(**kwargs)
            self.department = department

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

lead = TeamLead(name="Ann", salary=5000, department="IT",
                programming_language="Python", team_size=5)
print(lead.name, lead.department, lead.programming_language, lead.team_size)

if hasattr(lead, "department") and hasattr(lead, "programming_language"):
    print("Test passed")
else:
    print("Test failed")


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width_param, height_param):
        self.__width = width_param
        self.__height = height_param

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__height + self.__width)

class Circle(Shape):
    def __init__(self, radius_param):
        self.__radius = radius_param

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

class Square(Shape):
    def __init__(self, side_param):
        self.__side = side_param

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side

rectangle, circle, square = Rectangle(3, 4), Circle(4), Square(4)
lst_of_figures = [rectangle, circle, square]
for figure in lst_of_figures:
    print(f"Area: {figure.area()}. Perimeter: {figure.perimeter()}")