# Importing Abstract Base Class tools
from abc import ABC, abstractmethod

# Base abstract class to represent any person in the university
class Person(ABC):
    def __init__(self, name, age):
        self._name = name  # protected attribute
        self._age = age

    # Abstract method that child classes must implement
    @abstractmethod
    def get_role(self):
        pass

    # Common method to get name and age
    def get_basic_info(self):
        return f"Name: {self._name}, Age: {self._age}"

    # Method to get full info including role
    def get_details(self):
        return f"{self.get_basic_info()}, Role: {self.get_role()}"

# Student class that inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self._student_id = student_id
        self._course = course

    # Role implementation
    def get_role(self):
        return "Student"

    # Additional info specific to student
    def get_student_info(self):
        return f"{self.get_details()}, Student ID: {self._student_id}, Course: {self._course}"

# Professor class that inherits from Person
class Professor(Person):
    def __init__(self, name, age, p_id, department):
        super().__init__(name, age)
        self._p_id = p_id
        self._department = department

    def get_role(self):
        return "Professor"

    def get_professor_info(self):
        return f"{self.get_details()}, Professor ID: {self._p_id}, Department: {self._department}"

# AdminStaff class that inherits from Person
class AdminStaff(Person):
    def __init__(self, name, age, staff_id, designation):
        super().__init__(name, age)
        self._staff_id = staff_id
        self._designation = designation

    def get_role(self):
        return "Admin Staff"

    def get_staff_info(self):
        return f"{self.get_details()}, Staff ID: {self._staff_id}, Designation: {self._designation}"


# University class to manage list of people
class University:
    university_name = "Stanford University"  # Class variable (common for all)

    def __init__(self):
        self.__people = []  # Private list to store Person objects

    def add_person(self, person: Person): # 'person:Person' is a kindo of annotation
        self.__people.append(person)  # Add student, professor, or admin staff

    def display_all(self):
        if not self.__people:
            print("No people registered yet.")
        else:
            for person in self.__people:
                print(person.get_details())

    @classmethod
    def get_university_name(cls):
        return cls.university_name

    @staticmethod
    def welcome_message():
        return "Welcome to the Stanford University Management System"

# Start of the program
print(University.welcome_message())
print("University:", University.get_university_name())

# Create University system object
u = University()

# Menu for user input
while True:
    print("\n--- University Menu ---")
    print("1. Register Student")
    print("2. Register Professor")
    print("3. Register Admin Staff")
    print("4. Display All People")
    print("0. Exit")

    ch = input("Choose an option: ")

    if ch == "0":
        print("Thank you! Exiting the system.")
        break

    elif ch == "1":
        # Input student details
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        student_id = input("Enter Student ID: ")
        course = input("Enter Course Name: ")
        s = Student(name, age, student_id, course)
        u.add_person(s)
        print("✅ Student Registered Successfully!")

    elif ch == "2":
        # Input professor details
        name = input("Enter Professor Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        dept = input("Enter Department: ")
        p = Professor(name, age, emp_id, dept)
        u.add_person(p)
        print("✅ Professor Registered Successfully!")

    elif ch == "3":
        # Input admin staff details
        name = input("Enter Staff Name: ")
        age = int(input("Enter Age: "))
        staff_id = input("Enter Staff ID: ")
        designation = input("Enter Designation: ")
        a = AdminStaff(name, age, staff_id, designation)
        u.add_person(a)
        print("✅ Admin Staff Registered Successfully!")

    elif ch == "4":
        # Display all people registered
        print("\n--- List of Registered People ---")
        u.display_all()

    else:
        print("❌ Invalid option. Please choose again.")
