# The default except block can handle any kind of exception.
try:
    a = int(input("Enter a number: "))
    print("Value of a:",a)
except ZeroDivisionError:
    print("Don't divide by zero")
except Exception as e:
    print(e)
print("END")

# Default except must be at the last of the program
# otherwise it leads to syntax error in the program