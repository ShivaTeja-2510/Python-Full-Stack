"""1. Question 1: Define a Class
Question: Define a class named Person with attributes name and age. Write a method display to print the name and age.
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name:{self.name}, Age:{self.age}")

name=input("Enter your name:")
age=int(input("Enter your age:"))
p=Person(name,age)
p.display()

