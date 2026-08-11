#Sets and Operations on sets

numbers={10,20,30}
names={"shiva","ramu","vara"}
print(numbers,names)

#creating sets
#empty sets
s=set()
print(s,type(s))

#duplicates values
s={1,3,2,2,3}
print(s,type(s))

#Membership operators
print(2 in s)
print(100 not in s)

#Union
a,b={1,2,3},{3,4,5}
print("After Union :",a|b)

#Intersection
print("After Intersection: ",a&b)

#Difference
print("After Difference :",a-b)

#Symmetric Difference
print("After Symmetric Difference :",a^b)

#Subset
c,d={1,2},{1,2,4,5}
print(c<=d)

#Superset
print(d>=c)

