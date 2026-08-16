#Dictionary Methods
d = {1:101,2:102,3:103,4:104}

#access methods
print(d.get(1))
print(*d.keys())
print(*d.values())
print(*d.items())

#adding and updating methods
d.update({5:105})
print(d)
print(d.setdefault(6,106))

#Removing methods
d.pop(1)
print(d)
d.popitem()
print(d)
d.clear()
print(d)
