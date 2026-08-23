def my_gen():
    yield "First yield"
    yield "Second yield"

'''It doesn't run the function but it prepares
Generator Function'''

m=my_gen()
print(m)
print(next(m))
print(next(m))
#print(next(m)) #Stop Iteration
