# Strings and its concepts

str1 = "Hello"
str2 = "World"
str3 = '''this is a multi-line
string example'''
print(str1,str2,str3)

#Operations on Strings

# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) # Output: Hello World

# Repetition
print("Python! " * 3) # Output: Python! Python! Python!

# Indexing
text = "Python"
print(text[0]) # Output: P (1st character)
print(text[-1]) # Output: n (last character)

# Slicing
print(text[0:3]) # Output: Pyt (from index 0 to 2)
print(text[:4]) # Output: Pyth (default start is 0)
print(text[2:]) # Output: thon (from index 2 to end)

# Membership
print('Pyt' in text) # Output: True
print('Java' not in text) # Output: True
