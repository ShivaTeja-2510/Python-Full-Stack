def sum_natural(n):
    if n==1:
        return 1
    return n+sum_natural(n-1)

if __name__=="__main__":
    n = int(input("enter a number:"))
    result=sum_natural(n)
    print(f"The sum of first {n} natural numbers is {result}")
    