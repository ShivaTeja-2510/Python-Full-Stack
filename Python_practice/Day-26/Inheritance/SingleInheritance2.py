class User:
    def Login(self):
        print("Everyone need to login...")

class Manager(User):
    def Manage_Users(self):
        print("Manager manages the users")

m=Manager()
m.Login()
m.Manage_Users()