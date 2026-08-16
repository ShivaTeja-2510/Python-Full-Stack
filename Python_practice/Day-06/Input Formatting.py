#Input Formating in Python
#String Input
name =input("enter your name: ")
print(name)

#Integer Input
n =int(input("enter a number: "))
print(n)

#Float Input
percentage = float(input("enter your percentage: "))
print(percentage)

#Input as List
names = input("enter student names with spaces: ").split()
print(names)

#Input as list(comma seperated)
names2 = input("enter student names with commas: ").split(',')
print(names2)

#Input as a list of integers
marks = list(map(int,input("enter marks: ").split()))
print(marks)

#Input as a list of Floats
prices = list(map(float,input("enter the prices of the products: ").split()))
print(prices)

#Input as a tuple
dimensions = tuple(map(int,input("Enter length,width,height: ").split()))
print(dimensions)

#Input as a set
emp_ids=set(map(int,input("enter employee ids: ").split()))
print(emp_ids)

#Input as a dictionary
profile = eval(input("enter your profile as a dictionary: "))
print(profile)

#Multiple Inputs with unpacking
username,password=input("enter username and password: ").split()
print("Username: ",username)
print("Password: ",password)
