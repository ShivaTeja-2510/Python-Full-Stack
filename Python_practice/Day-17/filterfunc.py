#filtering the even from a list of numbers
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print("The even numbers are:",result)

#filtering odd numbers from a list of numbers
result1 = list(filter(lambda x: x % 2 != 0, numbers))
print("The odd numbers are:",result1)

#Products Above ₹1000
prices = [500, 1200, 800, 2500, 600]
result3 = list(filter(lambda price: price > 1000, prices))
print("The prices that are above 1000 are:",result3)

#Long Usernames
users = ["teja", "codegnan", "admin123", "raj"]
result4 = list(filter(lambda user: len(user) > 5, users))
print("the long usernames are:",result4)

