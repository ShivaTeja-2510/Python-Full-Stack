#program to find the count of prime digits in a given number
n = int(input("Enter a number: "))
count = 0
for digit in str(n):
    if digit in '2357':
        count += 1
print("Count of prime digits:", count)
