"""-----------------------------------------------------
Question 10: Polymorphism
Question: Define a base class Shape with a method area. Define derived classes Square and Triangle with their own implementations of the area method.
"""

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5*self.base*self.height

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*(self.side)

side=float(input("Enter the side of the square: "))
square=Square(side)
base=float(input("Enter the base of the triangle: "))
height=float(input("Enter the height of the triangle: "))
triangle=Triangle(base,height)
print(f"Area of the Square is {square.area()}")
print(f"Area of the Triangle is {triangle.area()}")