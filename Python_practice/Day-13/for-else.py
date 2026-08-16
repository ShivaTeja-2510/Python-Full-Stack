#in for-else the else will be executed if the for loop is not terminated by a break statement and the loop completes normally. If the for loop is terminated by a break statement, the else block will not be executed.

ids=[101,102,103,104]
key=108
for i in range(len(ids)):
    if ids[i]==key:
        print("Key found")
        break
else:
    print("Key not found")
print("End of the program")