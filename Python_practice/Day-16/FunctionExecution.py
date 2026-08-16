# A complete function execution tracking.

print("Start-1")

def add(a,b):
    print("Start-3")
    c=a+b
    return c
    print("end-1")

print("Start-2")
result=add(10,20)
print(result)
print("end")