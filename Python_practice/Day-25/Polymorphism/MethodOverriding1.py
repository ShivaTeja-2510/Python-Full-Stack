class Media:
    def Show(self):
        print("This is the Media Class")

class Book(Media):
    def Show(self):
        print("We read books")

b=Book()
b.Show()

'''Here, The parent class method will get 
overidden by the child class method'''
