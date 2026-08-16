#User Defined Function
def Greet1():
    print("Welcome to Functions in Python")
Greet1()

print("="*90)

def Greet(name,age):
    print("Hello",name,"! You are",age,"years old.")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
Greet(name,age)
