def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Mul(a,b):
    return a*b
def Div(a,b):
    if b!=0:
        return a/b
    return "provide a valid input"

if __name__ == "__main__":
    print(Add(1,3))
    print(Subtract(20,10))
