class Student:
    def __init__(self, name_param: str, last_name_param: str, age_param: int, avg_grade_param: int | float):
        self.name = name_param
        self.last_name = last_name_param
        self.age = age_param
        self.avg_grade = avg_grade_param

    def set_new_avg_grade(self, value: int | float):
        if isinstance(value, int | float):
            if value >= 0:
                self.avg_grade = value
            else:
                raise ValueError("You can't set negative numbers")
        else:
            raise TypeError("You can't set text")

    def print_data_about_student(self):
        print(f"Full name: {self.name} {self.last_name}. Age: {self.age}. \nAverage grade: {self.avg_grade}\n")


student_john = Student("John", "Doe", 19, 90)

student_john.print_data_about_student()
student_john.set_new_avg_grade(95.5)
student_john.print_data_about_student()
