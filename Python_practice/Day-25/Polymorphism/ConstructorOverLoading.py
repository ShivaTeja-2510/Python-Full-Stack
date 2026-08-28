class Test:
    def __init__(self):
        print("No Arguments constructor")

    def __init__(self,a):
        print("one argument constructor")

t=Test(10) # object creation invokes the ultimate constructor in the class