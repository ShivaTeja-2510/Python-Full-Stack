def my_gen():
    print("one")
    yield "First yield"
    print("two")
    yield "Second yield"
    print("three")

'''It doesn't run the function but it prepares
Generator Function'''

m=my_gen()
print(m)
print(next(m))
print(next(m))
#print(next(m)) #Stop Iteration
