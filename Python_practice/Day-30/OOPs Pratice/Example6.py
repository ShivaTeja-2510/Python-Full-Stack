"""Question 6: Class Method
Question: Define a class Circle with a class method to calculate the area given the radius.
"""
import math


class Circle:
    @classmethod
    def area(cls, radius):
        return math.pi * (radius ** 2)

radius=float(input("Enter the radius of the circle: "))
print(f"Area of the circle is {Circle.area(radius)}")
