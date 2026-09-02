"""Question 18: Hierarchical Inheritance
Question: Create a base class Vehicle with an attribute brand. Create two derived classes Car and Bike that inherit Vehicle and add their own attributes.
"""

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Bike(Vehicle):
    def __init__(self, brand, type_bike):
        super().__init__(brand)
        self.type_bike = type_bike

    def display(self):
        print(f"Brand: {self.brand}, Type: {self.type_bike}")

# Taking input from user
brand = input("Enter brand: ")
model = input("Enter model for car: ")
type_bike = input("Enter type for bike: ")

car = Car(brand, model)
bike = Bike(brand, type_bike)

print("Car Details:")
car.display()
print("Bike Details:")
bike.display()
