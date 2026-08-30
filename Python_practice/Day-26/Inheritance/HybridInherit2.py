class Person:
    def Work(self):
        print("A Person Works in an MNC")

class Employee(Person):
    def Manage(self):
        print("A Employee Manages activities in an MNC")

class Developer(Employee):
    def Develop(self):
        print("A Developer develops code")

class Trainer(Developer):
    def Train(self):
        print("A Trainer trains the freshers and trainees")

t=Trainer()
t.Train()
t.Develop()
d=Developer()
d.Develop()
d.Manage()
d.Work()
