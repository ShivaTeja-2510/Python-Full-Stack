class Student:
    college="CodeGnan"
    def __init__(self):
        self.name="Ramu"
        self.age=23
        self.marks=90

    # Class Method ----> @classmethod
    @classmethod
    def Show(cls):
        print("my college name is:",cls.college)

s=Student()
Student.Show() #First way to access class method
s.Show()       #Second way to access class method