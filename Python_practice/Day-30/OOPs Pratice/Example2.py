"""2. Question 2 Class with Multiple Methods
Question: Define a class named Rectangle with attributes length and width. Write methods to calculate the area and the perimeter."""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)
print(f"The area of the rectangle is: {rectangle.area()}")
print(f"The perimeter of the rectangle is: {rectangle.perimeter()}")