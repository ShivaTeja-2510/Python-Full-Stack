class Employee:
    def __init__(self, name):
        self.name = name

    def Show(self):
        print("Employee Name is:", self.name)


class Manager(Employee):
    def __init__(self, name, dept):
        super().__init__(name)
        self.dept = dept

    def Show(self) -> None:
        super().Show()
        print("My Dept name is:", self.dept)

m = Manager("Shiva", "Computer Science")
m.Show()
