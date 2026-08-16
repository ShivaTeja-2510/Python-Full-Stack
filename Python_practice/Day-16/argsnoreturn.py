#with arguments and without return value

def add(a,b):
    print("Addition of a and b is: ", a + b)
a,b=map(int, input("Enter two numbers separated by space: ").split())
add(a,b)