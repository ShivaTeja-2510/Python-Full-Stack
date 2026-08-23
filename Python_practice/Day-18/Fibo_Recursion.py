def Fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return Fibo(n-2)+Fibo(n-1)

if __name__=="__main__":
    n = int(input("enter a number: "))
    result=Fibo(n)
    print(f"The {n+1}th fibonacci number is {result}")
    print(f"The Fibonacci series upto {n} is",end=" ")
    for i in range(n):
        print(Fibo(i),end=" ")