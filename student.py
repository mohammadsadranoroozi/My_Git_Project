class Student:
    def __init__(self, name):
        self.name = name
    def get_info(self):
        return f"Student name is {self.name}"
my_student = Student("Mohammadsadra Noroozi")
