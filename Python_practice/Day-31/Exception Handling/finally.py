# The default except block can handle any kind of exception.
try:
    a = int(input("Enter a number: "))
    print("Value of a:",a)
except ZeroDivisionError as e:
    print("Don't divide by zero",e)
except ValueError as e:
    print("Invalid input",e)
finally:
    print("I am always executed for you..")
print("END")

# Default except must be at the last of the program
# otherwise it leads to syntax error in the program
# When shut down the PVM, the finally block doesn't get executed
# we use os.exit(0) to shut down the PVM