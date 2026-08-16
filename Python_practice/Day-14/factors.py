n = int(input("Enter number: "))

factors = []

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        factors.append(i)

        if i != n // i:
            factors.append(n // i)

factors.sort()

print("Factors:", *factors)

if len(factors) == 2:
    print(f"{n} is a prime number.")

else:
    print(f"{n} is a composite number.")

