"""Question 13: Operator Overloading
Question: Define a class Vector that supports addition using the + operator
"""

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __str__(self) -> str:
        return f"Vector({self.x},{self.y})"

x1=float(input("Enter the first value:"))
y1=float(input("Enter the first value:"))
x2=float(input("Enter the second value:"))
y2=float(input("Enter the second value:"))
vector1=Vector(x1,y1)
vector2=Vector(x2,y2)
res=vector1+vector2
print(f"Result: {res}")