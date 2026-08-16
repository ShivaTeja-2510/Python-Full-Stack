n = int(input())
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if temp==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

    '''Using a String
    '''
'''s = str(temp)
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")'''