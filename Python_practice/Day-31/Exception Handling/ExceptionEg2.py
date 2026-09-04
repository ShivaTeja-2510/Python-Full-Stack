try:
    a=10
    b=2
    print("Execution Started")
    print(a+b)
    print(a-b)
    print(a/0)
    print(a*b)
    """whenever the exception is raised then
                the remaining statements will never be executed"""
except ZeroDivisionError as e:
    print("Please don't divide by Zero")
print("Execution Stopped")

#If there is no exception in the try block ,
#no except block will be executed