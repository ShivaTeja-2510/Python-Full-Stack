#printing patterns of alphabets like this
''' A B C
    A B C
    A B C'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print(chr(65 + j), end=" ")
    print()
#===============================================================================
#printing patterns of alphabets like this
''' A A A
    B B B
    C C C'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print(chr(65 + i), end=" ")
    print()
#===============================================================================
#Printing the alphabets like this
'''A B C
   D E F
   G H I'''
n = int(input("Enter a number: "))
k = 0
for i in range(n):
    for j in range(n):
        print(chr(65 + k), end=" ")
        k += 1
    print()
#===============================================================================
'''A
   B B
   C C C'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()






































































































































































































