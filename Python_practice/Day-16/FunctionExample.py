#Without Function(Performing Addition)
a,b = 10, 20
print("Addition of a and b without using function is: ", a + b)
    
print("="*90)

#With Function(Performing Addition)
def add(x, y):
    return x + y
x,y=map(int, input("Enter two numbers: ").split())
print("Addition of x and y using function is: ", add(x, y))