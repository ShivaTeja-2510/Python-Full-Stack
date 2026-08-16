num = 10
def Update():
    global num
    num=100
    print("Number inside the function:",num,id(num))
print("Start")
Update() #the function is being called
print("End of the function")
print("Number outside the function:",num,id(num))
