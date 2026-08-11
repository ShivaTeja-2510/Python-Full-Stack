s = input("Enter string: ")

count = 0

for char in s:
    if char.lower() in "aeiou":
        count += 1

print("Number of vowels =", count)


'''
s = input("Enter string: ")

count = sum(1 for char in s if char.lower() in "aeiou")

print("Number of vowels =", count)'''
