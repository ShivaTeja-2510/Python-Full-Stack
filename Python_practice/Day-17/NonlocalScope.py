#NON-LOCAL SCOPE IS USED IN NESTED FUNCTIONS 
def Outer():
    def Inner():
        print("Inner Function")
    Inner()
    print("Outer Function")
print("Start")
Outer()
print("End")