class A:
    def M1(self):
        print("M1() in class A")

class B(A):
    def M2(self):
        print("M2() in class B")

class C(A):
    def M3(self):
        print("M3() in class C")   #Upto here Hierarchical Inheritance

class D(B,C):
    def M4(self):
        print("M4() in class D")

d=D()
d.M1()
d.M2()
d.M3()
d.M4()