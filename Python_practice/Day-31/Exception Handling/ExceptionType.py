try:
    a=int(input("Enter a number:"))
    b=int(input("Enter another number:"))
    res=a/b
    print("result is ",res)
except ZeroDivisionError as e:
    print("Exception Type:",type(e))
    print("Exception Message;",e)
    print("Exception class name:",e.__class__.__name__)
    print("Exception Data:",e.__class__)