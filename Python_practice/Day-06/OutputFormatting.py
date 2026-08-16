#printing the statement
print("Hello world!")
#printing multiple objects or variables
name,rollno = "shiva",67
print(name,rollno)
#printing using a seperator
print("2026","03","08",sep="-")
#priting using end keyword
print("Hello,",end=" ")
print("World")
#using \n in print()
print("Line1\nLine2")
#using \t in print()
print("Name:\tShiva")
#Printing using modulo % operator
name="Shiva"
age=21
score=99.6
print("Name: %s | Age:%d | Score: %.2f"%(name,age,score))
#Using f-strings
name="Charlie"
age=28
score=98.3
print(f"Name:{name} | Age:{age} | Score:{score:.2f}")
#Using s.format()
name="Diana"
age=22
score=89.456
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age,score))

