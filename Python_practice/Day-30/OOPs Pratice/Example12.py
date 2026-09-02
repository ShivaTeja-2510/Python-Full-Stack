"""Question 12: Method Overriding
Question: Define a base class Animal with a method sound. Define derived classes Dog and Cat that override the sound method.
"""

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animal_type=input("Enter animal type:")
if animal_type=="Dog":
    animal=Dog()
elif animal_type=="Cat":
    animal=Cat()
else:
    print("Invalid animal type")
    animal=None
if animal:
    print(f"Sound: {animal.sound()}")