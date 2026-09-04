# try-except with else
try:
    a=int(input("Enter a value: "))
    b=int(input("Enter b value: "))
    result=a/b
except ZeroDivisionError as e:
    print("Don't divide by zero")
    print("Exception Message is:",e)
else:
    print("No Exception is try block, due to that i am getting executed")
    print("Result:",result)
print("END")