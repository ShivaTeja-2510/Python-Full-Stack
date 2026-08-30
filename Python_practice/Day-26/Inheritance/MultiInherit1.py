class Father:
    def Work(self):
        print("Father works")

class Mother:
    def Makes(self):
        print("Mother makes food")

class Child(Father,Mother):
    def Play(self):
        print("Child plays")

c=Child()
c.Makes()
c.Work()
c.Play()