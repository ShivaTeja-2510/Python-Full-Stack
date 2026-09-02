"""Question 14: Function Overloading Using Default Arguments
Question: Define a function greet that can greet a person by their name or simply say "Hello" if no name is provided.
"""

def greet(name=""):
    if name:
        return f"Hello,{name}!"
    else:
        return "Hello!"
name=input("Enter your name:")
print(greet(name))