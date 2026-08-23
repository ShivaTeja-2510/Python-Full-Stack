#Intuition with Using Functions in
#terms of memory usage to proceed with Generators.

def greet():
    return "Good Morning"

print(greet())

def square(l):
    k=[]
    for i in l:
        k.append(i*i)
    return k

list1=list(map(int,input("enter the numbers: ").split()))
r=square(list1)
print(*r)