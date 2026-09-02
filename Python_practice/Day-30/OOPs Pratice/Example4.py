"""Question 4: Class with Default Values
Question: Define a class Employee with attributes name and salary. Set the default value of salary to 50000 if not provided.
"""

class Employee:
    def __init__(self,name,sal=50000):
        self.name=name
        self.sal=sal

    def display(self):
        print(f"Employee Name:{self.name}, Salary:{self.sal}")


name=input("Enter Employee Name:")
sal=input("Enter Employee Salary:")
emp=Employee(name,sal)
emp.display()