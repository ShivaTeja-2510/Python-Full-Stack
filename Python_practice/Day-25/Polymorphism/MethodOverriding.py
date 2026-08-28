class Test:

    def Add(self, a, b):
        return f"the sum of {a} and {b} is {a+b}"

    def Add(self, a, b, c):
        return f"the sum of {a},{b} and {c} is {a+b+c}"

t=Test()
# print(t.Add(10,30))
# #It raises a type error here because the pvm executes only the last method declared.
print(t.Add(10,20,30))
