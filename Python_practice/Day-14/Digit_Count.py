#Counting the number of digits in a given number
n = int(input("Enter a number: "))
#print("Number of digits in", n, "is", len(str(n)))
for i in str(n):
    count = len(str(n))
print(f"Number of digits in {n} is {count}")