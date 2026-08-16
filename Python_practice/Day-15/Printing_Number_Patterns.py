#Printing the numbers like this
''' 1
    2 2
    3 3 3
    4 4 4 4'''
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
#================================================================================
#Printing the numbers like this
'''1
   1 2
   1 2 3
   1 2 3 4'''
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#===============================================================================
#Printing the numbers like this
'''
    1
    2 3
    4 5 6
    7 8 9 10'''
n = int(input("Enter a number: "))
k = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(k, end=" ")
        k += 1
    print()
#===============================================================================
#Printing the numbers like this
'''
    4 4 4 4
    3 3 3
    2 2
    1'''
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()