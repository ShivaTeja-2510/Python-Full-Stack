"""Question 18: Multiple Inheritance
Question: Create two base classes Teacher and Researcher. Create a derived class Professor that inherits both Teacher and Researcher.
"""

class Teacher:
    def __init__(self, subject):
        self.subject = subject

class Researcher:
    def __init__(self, field):
        self.field = field

class Professor(Teacher, Researcher):
    def __init__(self, subject, field, name):
        Teacher.__init__(self, subject)
        Researcher.__init__(self, field)
        self.name = name

    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}, Field: {self.field}")

# Taking input from user
name = input("Enter name: ")
subject = input("Enter subject: ")
field = input("Enter research field: ")
professor = Professor(subject, field, name)
professor.display()
