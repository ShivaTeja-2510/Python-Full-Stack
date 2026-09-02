"""Question 19: Hybrid Inheritance
Question: Create a base class Animal with a method speak(). Create two derived classes Bird and Mammal that inherit Animal. Create another derived class Bat that inherits both Bird and Mammal.
"""

class Animal:
    def speak(self):
        return "Animal Sound"

class Bird(Animal):
    def speak(self):
        return "Chirp"

class Mammal(Animal):
    def speak(self):
        return "Mammal Sound"

class Bat(Bird, Mammal):
    def speak(self):
        return f"Bat Sound (inherits {Bird.speak(self)} and {Mammal.speak(self)})"

bat = Bat()
print(bat.speak())
