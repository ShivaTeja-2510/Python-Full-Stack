class Student:
    college="CodeGnan"
    def __init__(self):
        self.name="Ramu"
        self.age=23
        self.marks=90

    # Instance Method
    def Talk(self):
        print("my name is:",self.name)
        print("my age is:",self.age)
        print("my marks are:",self.marks)

s=Student()
s.Talk()  #we can call the instance method by using the reference variable
