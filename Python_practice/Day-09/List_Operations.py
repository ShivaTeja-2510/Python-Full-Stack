#Lists and the operations on lists

numbers=[10,20,30]
print(numbers,type(numbers)) # Output: [10, 20, 30] <class 'list'>

#Concatenation
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c) # Output: [1, 2, 3, 4, 5, 6]

#Repetition
print(a*3) # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

#Indexing
print(numbers[0]) # Output: 10 (1st element)
print(numbers[-1]) # Output: 30 (last element)
print(numbers[2])

#Slicing
print(numbers[0:2]) # Output: [10, 20] (from index 0 to 1)
print(numbers[:2]) # Output: [10, 20] (default start is 0)
print(numbers[1:3]) # Output: [20, 30] (from index 1 to 2)
print(numbers[::-1]) # Output: [30, 20, 10] (reversed list)

#Membership Operators
print(20 in numbers) # Output: True
print(40 not in numbers) # Output: True