#This is an example for positional only arguments in python. Positional only arguments are those arguments which can be passed only by position and not by keyword. In python, we can define positional only arguments by using / in the function definition.
def add(a, b, /):
    return a + b

# This will work
result = add(5, 10)
print(result)  # Output: 15

# This raises a TypeError
'''result = add(a=5, b=10)
print(result)'''  # Output: TypeError because these are keyword arguments and we have defined the function to accept only positional arguments.