#A Global Scope can be accessed
#anywhere within the python code.
company = "Codegnan"
def Display():
    print("Inside Function: ",company)
print("Start-1")
Display()
print("Outside Function: ",company)
print("Start-2")