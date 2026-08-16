#print the stars like this
'''  
       * * * 
        * * 
         * 
        * * 
       * * *  '''
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
for i in range(2, n + 1):
    print(" " * (n - i) + "* " * i)
#================================================================================
#printing the stars like this
'''  *
     *
 * * * * *
     *
     * '''
n = int(input("Enter a number: "))
for i in range(n):
    if i == n // 2:
        print("* " * n)
    else:
        print("  " * (n // 2) + "*")
#================================================================================
#printing the stars like this
'''  * * * * *
     *       *
     *       *
     *       *
     * * * * * '''
n = int(input("Enter a number: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print("* " * n)
    else:
        print("*" + " " * (2 * n - 3) + "*")
#================================================================================
#printing the stars like this
'''  *       *
       *   *  
         *    
       *   * 
     *       * '''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()