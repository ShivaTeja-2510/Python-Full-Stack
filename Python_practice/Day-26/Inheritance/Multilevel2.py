class Employee:
    def Work(self):
        print("Working")

class Developer(Employee):
    def Develop(self):
        print("Write the Code")

class Intern(Developer):
    def Learn(self):
        print("Learning")

i=Intern()
i.Learn()
i.Develop()
i.Work()