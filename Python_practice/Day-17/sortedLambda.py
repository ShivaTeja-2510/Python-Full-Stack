#Using the usual sorted() method and priting the result
numbers=[10,3,4,2,6,5]
result=sorted(numbers)
print("sorted numbers :",result)

print("="*100)

#Now sorting a list of tuples using the lambda function

students = [
   ("Rahul", 80),
   ("Anil", 95),
   ("Kiran", 70),
   ("Suresh", 85)
]

result = sorted(students, key=lambda x: x[1])

print("Sorted list of tuples using lambda function based on marks:",result)
