#squaring numbers of a list
numbers=[1,2,3,4,5,6]
result=list(map(lambda x:x*x, numbers))
print('the square of the numbers of the list:',result)

#Convert Names to Uppercase
names = ["teja", "ravi", "sneha"]
result = list(map(lambda name: name.upper(), names))
print("the uppercase form of the names:",result)

#Calculate String Length
words = ["python", "java", "sql"]
result = list(map(lambda word: len(word), words))
print("the corresponding lengths of the strings are:",result)