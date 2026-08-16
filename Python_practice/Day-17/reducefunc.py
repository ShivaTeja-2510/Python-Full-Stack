#Sum of the numbers of a list
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, numbers)
print("The sum of the numbers:",result)

#Product of the numbers of a list
numbers = [1, 2, 3, 4]
result = reduce(lambda a, b: a * b, numbers)
print("The product of the numbers:",result)

#Largest Number
numbers = [10, 25, 8, 40, 15]
result = reduce(lambda a, b: a if a > b else b, numbers)
print("The largest number is:",result)