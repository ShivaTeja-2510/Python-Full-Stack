"""Question 7: Static Method
Question: Define a class MathOperations with a static method to calculate the factorial of a number.
"""

class MathOperations:
    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * MathOperations.factorial(n-1)

n=int(input("Enter the number: "))
print(f"Factorial of {n} is {MathOperations.factorial(n)}")
