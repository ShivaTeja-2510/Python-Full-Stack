a=10
b=2
print("Execution Started")
print(a+b)
print(a-b)
print(a*b)
try:
    print(a/0)
except ZeroDivisionError as e:
    print("You can't divide a number by zero")
print("Execution Stopped")
# In this case without any exceptions, this print statement doesn't execute, because it terminates
# For this we use exception handling to achieve normal termination.