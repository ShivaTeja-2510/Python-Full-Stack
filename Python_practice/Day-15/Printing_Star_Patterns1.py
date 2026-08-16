# Output: *** (3 stars printed without space in between)
print("*"*3,sep=" ")

print("="*90)

# Output: * * * (3 stars printed with space in between)
print(*["*" for i in range(3)], sep=" ") 
"""printing the basic star pattern
        * * * *
        * * * * """

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()  

"""Printing the patterns using rows and columns"""
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
for i in range(n):
    for j in range(m):
        print("*", end=" ")
    print()

"""Printing the stars like this
    *
    * *
    * * *
    * * * * """
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()

"""Printing the stars like this
             *
           * *
         * * *
       * * * * """
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()