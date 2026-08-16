#Basic Function for squaring a number
def square(x):
    return x * x

print(f"The Square of the number is {square(int(input('Enter a number: ')))}")

print("=" * 100)

# Squaring the number using lambda function
n = int(input("Now Enter another number: "))
sqr = lambda x: x ** 2
print(f"The square of {n} using Lambda function is: {sqr(n)}")