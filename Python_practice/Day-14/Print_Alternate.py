#program to print the digits of a number in alternate order from forward direction and backward direction
n = int(input("Enter a number: "))
digits = str(n)
for i in range(0, len(digits), 2):
    print(digits[i], end=" ")
for i in range(len(digits)-1, -1, -1):
    if i % 2 == 1:
        print(digits[i], end=" ")