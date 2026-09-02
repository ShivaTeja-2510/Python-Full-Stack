"""Question 9: Encapsulation
Question: Define a class Student with attributes name and marks. Use getter and setter methods to access and modify the marks.
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks
# Taking input from user
name = input("Enter name: ")
marks = int(input("Enter marks: "))
student = Student(name, marks)
print(f"Initial Marks: {student.get_marks()}")
new_marks = int(input("Enter new marks: "))
student.set_marks(new_marks)
print(f"Updated Marks: {student.get_marks()}")
