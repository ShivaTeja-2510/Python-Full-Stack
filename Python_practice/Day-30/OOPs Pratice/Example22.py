"""Question 20: Using super() to Call Parent Method
Question: Create a base class Employee with a method work(). Create a derived class Manager that overrides work() but also calls the parent work() method.
"""

class Employee:
    def work(self):
        return "Employee working"

class Manager(Employee):
    def work(self):
        base_work = super().work()
        return f"{base_work} and managing"

manager = Manager()
print(manager.work())
