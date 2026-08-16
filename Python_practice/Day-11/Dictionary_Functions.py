#Built-in dictionary functions
employee={'name':'shiva','eid':101,"batch":"pfs-064"}
print(employee,type(employee))

print(len(employee))
print(max(employee))
print(min(employee))
print(sorted(employee))
print(dict(id=101,name='shiva',course='python'))
print(any(employee))
print(all(employee))

#Nested Dictionaries
students = {
"s1": {"name": "Ravi", "age": 22 },
"s2": {"name": "Teja","age": 21}
}
print(students["s1"]["name"]) # Ravi

#mutable values inside dictionaries
student = {
"marks": [90, 85, 88]
}
student["marks"].append(95)
print(student)
{'marks': [90, 85, 88, 95]}
