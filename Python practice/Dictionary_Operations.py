#Dictionary
#creating dictionaries
data={}
data=dict()
print(data,type(data))

#dictionary with values
student={"name":"shiva","age":21,"course":"Python"}
print(student,type(student))

#using dict()
student=dict(id=101,name="Shiva",Course="Python")
print(student,type(student))

#Dictionary Operations
#Accessing the values
print(student['name'])
print(student['id'])

#updating values in the dictionary
student["age"]=23
print(student)

#adding new key value pairs
student = { "name": "Ravi"}
student["course"] = "Python"
print(student)

#removing items
student = {
"name": "Ravi",
"age": 22
}
del student["age"]
print(student)

#Membership Operators
print('name' in student)
print('course' not in student)
