# Using Single try, Multiple except blocks
# Only one exception is raised in the try block at a time *****

try:
    print("Execution Started")
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    result=a/b
    print("Result is:",result)
except ZeroDivisionError as e:
    print("You cannot divide by zero")
    print("Exception Message is:",e)
except ValueError as e:
    print("Invalid Input, Please enter a valid integer")
    print("Exception Message is:",e)
print("Execution Finished")