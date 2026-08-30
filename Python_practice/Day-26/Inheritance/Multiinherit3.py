class A:
    def m1(self):
        print("I am m1() in class-A")

class B:
    def m1(self):
        print("I am m1() in class-B")

class C(A,B):   # It follows MRO (Method Resolution Order)
    pass
    #def m1(self):
        #print("I am m1() in class-C")

c=C()
c.m1()
print(C.__mro__)