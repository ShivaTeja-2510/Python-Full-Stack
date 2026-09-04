# Example for ValueError Exception

try:
    print("Execution Started")
    a=int(input("Enter a number:"))
    print("hey")
except ValueError as e:
    print("Invalid Input, Please enter an integer")
print("Execution Stopped")
