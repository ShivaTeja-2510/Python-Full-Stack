def square(l):
    for i in l:
        yield i*i

n=list(map(int,input().split()))
s=square(n)
print(s)
for i in s:
    print(i)