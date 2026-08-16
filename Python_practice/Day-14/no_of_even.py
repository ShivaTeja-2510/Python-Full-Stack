n = int(input("enter a number:"))
'''s = str(n)
count = 0
for i in s:
    if int(i) % 2 == 0:
        count += 1
print(f"count of even digits in {n} is {count}")'''
res=len(list(i for i in str(n) if int(i)%2==0))
print(f"count of even digits in {n} is {res}")