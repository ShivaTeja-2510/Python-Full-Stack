#List Built-in methods

lst=[10,20]
print("Original List: ",lst)

#appending element to a list
lst.append(30)
print("After Appending: ",lst)

#extending the list with another sublist
lst.extend([40,50])
print("After extending: ",lst)

#inserting an element at a specified position
lst.insert(1,10)
print("After inserting: ",lst)

#removing the first occurance of an element
lst.remove(10)
print("After removing: ",lst)

#poping the element using index
lst.pop(4)
print("After popping: ",lst)

#clearing the element in the list
lst.clear()
print("After Clearing: ",lst)

lst.extend([10,40,20,40,30,40])
print("After Recreation: ",lst)

#searching the element using index
print(lst.index(20))

#counting the occurances
print(lst.count(40))

#sorting the list
lst.sort()
print("After sorting: ",lst)

#reversing the list
lst.reverse()
print("After reversing :",lst)

lst.copy()
print(lst)

del lst


