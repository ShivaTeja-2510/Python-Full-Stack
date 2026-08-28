"""In python , Method-overloading can be achieved
by using the default parameters or the arbitrary
arguments"""
class Test:
    def Add(self, *l):
        sum = 0
        for i in l:
            sum+=i
        print(f"The Sum is {sum}")

t=Test()
t.Add(10)
t.Add(10,20)
t.Add(10,20,30)