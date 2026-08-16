'''the enclosing scope in the inner function
in the nested function can be made using the 
nonlocal keyword'''
x=100
def Outer():
    x=10
    print("Inside the Outer:",x)
    def Inner():
        nonlocal x
        x=1000
        print("Inside the Inner:",x)
    Inner()
    print("Outside the Inner:",x)
print("start-1")
Outer()
print("Outside the Outer:",x)