"""Question 16: Method Overriding with Different Arguments
Question: Define a base class Calculator with a method calculate that takes two integers. Define a derived class AdvancedCalculator that overrides calculate to take three integers.
"""
class Calculator:
    def calculate(self,x,y):
        return (x+y)

class AdvancedCalculator(Calculator):
    def calculate(self,x,y,z):
        return x+y+z

calc_type=input("Please enter calculation type:")
if calc_type == "basic":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    calculator = Calculator()
    print(f"Result: {calculator.calculate(a, b)}")
elif calc_type == "advanced":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    calculator = AdvancedCalculator()
    print(f"Result: {calculator.calculate(a, b, c)}")
else:
    print("Invalid calculator type")