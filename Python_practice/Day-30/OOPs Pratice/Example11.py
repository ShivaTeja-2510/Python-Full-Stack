"""Question 11: Polymorphic Method in Class
Question: Define a base class Shape with a method area. Define derived classes Square and Circle that implement their own versions of area.
"""
import math


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius**2

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2

shape_type=input("Enter the type of Shape: ")
if shape_type=="Square":
    side=float(input("Enter the side of the Square: "))
    shape=Square(side)
elif shape_type=="Circle":
    radius=float(input("Enter the radius of the Circle: "))
    shape=Circle(radius)
else:
    print("Invalid Shape Type")
    shape=None
if shape:
    print(f"Area: {shape.area()}")