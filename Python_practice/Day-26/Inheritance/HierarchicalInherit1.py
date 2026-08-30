class Vehicle:
    def Fuel_type(self):
        print("Uses petrol or diesel or gas")

class Car(Vehicle):
    def Drive(self):
        print("Driving")

class Bike(Vehicle):
    def Ride(self):
        print("Riding")

b=Bike()
c=Car()
c.Drive()
b.Ride()
b.Fuel_type()