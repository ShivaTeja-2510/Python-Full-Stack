"""Question 17: Multilevel Inheritance
Question: Create a base class Person with attributes name and age. Create a derived class Employee that inherits Person and adds an attribute salary. Create another derived class Manager that inherits Employee and adds an attribute department.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Department: {self.department}")

# Taking input from user
name = input("Enter name: ")
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
department = input("Enter department: ")

manager = Manager(name, age, salary, department)
manager.display()
