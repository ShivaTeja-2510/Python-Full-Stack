class Animal:
    def Eat(self):
        print("Eating")

class Dog(Animal):
    def Bark(self):
        print("Barking")

class BabyDog(Dog):
    def Cry(self):
        print("Crying")

b=BabyDog()
b.Cry()
b.Bark()
b.Eat()
