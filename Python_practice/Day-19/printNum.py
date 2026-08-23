#Printing the numbers from 1 to 5 using generator.
def numbers():
    for i in range(1,6):
        yield i
n=numbers()
for i in range(1,6):
    print(i)  #For loop internally calls next()