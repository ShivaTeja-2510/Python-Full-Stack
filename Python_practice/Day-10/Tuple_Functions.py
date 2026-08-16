#Tuple Built-in Functions,Methods,Packing and Unpacking

t = (10,40,30,20,12)

#len()
print(len(t))
#max()
print(max(t))
#min()
print(min(t))
#sum()
print(sum(t))
#sorted()
print(sorted(t))
#tuple()
print(tuple("shiva"),tuple(['python','full stack']))
#any()
print(any((0,0,1)))
#all()
print(all((1,2,4)))

#Tuple Built-in Methods
#count()
t1=(10,20,10,20,30,40,50)
print(t1.count(20))

#index()
print(t1.index(10))

#Tuple Packing and Unpacking
data = 10,20,30
print("After Packing: ",data)
a,b,c =(10,20,30)
a,b,c=data
print("After Unpacking: ",a,b,c)

#nested tuples
data = ((1, 2), (3, 4))
print(data[0]) # (1, 2)
print(data[1][1]) # 4


