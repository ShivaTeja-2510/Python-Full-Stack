# Nested try-except
try:
    a = int(input("Enter a number: "))
    try:
        b= int(input("Enter another number:"))
        result = a/b
        print("Result is:",result)
    except ZeroDivisionError as e:
        print("Don't divide by zero")
except ValueError:
    print("Invalid Input, Please enter a valid integer")
print("END")