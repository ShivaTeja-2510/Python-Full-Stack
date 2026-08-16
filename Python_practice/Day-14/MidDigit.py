#Program to find out the middle digit of a given number and also mention when the user input is invalid for even number of digits
n = int(input("Enter a number: "))
digits = str(n)
if len(digits) % 2 == 1:
    middle_index = len(digits) // 2
    middle_digit = digits[middle_index]
    print("Middle digit:", middle_digit)
else:
    print("Invalid input: The number has an even number of digits.")