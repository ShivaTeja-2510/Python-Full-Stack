#Set Methods
s={10,20,20,30,40}

#adding one element to the set
s.add(50)
print("After adding :",s)

#adding multiple elements to the set
s.update({60,70})
print("After updating :",s)

#removing the element from the set
s.remove(10)
print(s)

#discarding the element from the set
s.discard(20)
print(s)

#popping the random element using pop()
s.pop()
print(s)

#FrozenSet
unique_ids=frozenset({10,20,30})
print("Frozen-set: ",unique_ids)
