class Animal:
    def Sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def Bark(self):
        print("Dog barks")

d=Dog()
d.Sound()
d.Bark()