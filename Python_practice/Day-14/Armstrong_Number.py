n = int(input())
temp = n
sum = 0
while n > 0:
    dig = n % 10
    sum += dig ** len(str(temp))
    n = n // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")