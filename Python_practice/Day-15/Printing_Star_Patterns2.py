#Printing the stars like this
''' *
   * *
  * * * '''
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
#================================================================================
#Printing the stars like this
''' * * *
     * *
      * '''

n = int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
#================================================================================
#Printing the stars like this
''' * * * *
    * * *
    * *
    * '''

n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(n - i):
        print("", end="")
    for k in range(i):
        print("*", end=" ")
    print()
#================================================================================
#Printing the stars like this
''' *
   * *
  * * *
 * * * *
  * * *
   * *
    * '''

n = int(input("Enter a number: "))
# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)


