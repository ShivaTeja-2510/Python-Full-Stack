from itertools import count,permutations,combinations

n=[1,2,3,4,4,4,3,3,3,2,2]
c=n.count(3)
print(c)

n1=permutations('abc',2)
print(list(n1))

n2=combinations('abc',2)
print(list(n2))