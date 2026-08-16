#Tuple

numbers = (10,20,30,40)
print(numbers,type(numbers)) # Output: (10, 20, 30, 40) <class 'tuple'>

#creating tuples
#emtpy tuple
t=()
print(t,type(t)) # Output: () <class 'tuple'>

#single element tuple****
t=(10,)
print(t,type(t)) # Output: (10,) <class 'tuple'>

t=(10)
print(t,type(t)) # Output: 10 <class 'int'>

#Concatenation
a,b = (1,2),(1,4)
c = a + b
print(c) # Output: (1, 2, 1, 4)

#Repetition
print(a*3) # Output: (1, 2, 1, 2, 1, 2)

#Indexing
data=(10,20,30,40)
print(data[0]) # Output: 10 (1st element)
print(data[-1]) # Output: 40 (last element)

#Slicing
print(data[0:2]) # Output: (10, 20) (from index 0 to 1)
print(data[:2]) # Output: (10, 20) (default start is 0)
print(data[0:3:2]) # Output: (10, 30) (from index 0 to 2 with step 2)
print(data[::-1]) # Output: (40, 30, 20, 10) (reversed tuple)

#Membership Operators
print(20 in data) # Output: True
print(50 not in data) # Output: True