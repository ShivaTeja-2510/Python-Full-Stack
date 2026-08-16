#program to find the sum of prime digits in a given number
n = int(input("Enter a number: "))
sum = 0
for digit in str(n):
    if digit in '2357':
        sum += int(digit)
print("Sum of prime digits:", sum)