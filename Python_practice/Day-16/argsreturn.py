#with arguments and with return value

def add(a,b):
    return a + b
a,b=map(int, input("Enter two numbers separated by space: ").split())
print("Addition of a and b is: ", add(a,b))