"""Question 17: Single Inheritance
Question: Create a base class Animal with an attribute name and a method speak(). Create a derived class Dog that inherits Animal and overrides the speak() method.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal Sound"
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Bowwww !"
# Taking input from user
name = input("Enter the name of the dog: ")
dog = Dog(name)
print(dog.speak())
