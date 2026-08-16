# This is an example for keyword only arguments in python. Keyword only arguments are those arguments which can be passed only by keyword and not by position. In python, we can define keyword only arguments by using * in the function definition.
def printDetails(*, name, age, city):
    print("Hello I am", name, "! I am", age, "years old and I live in", city)
printDetails(name="Shiva",age=21,city="Hyd")
'''printDetails(name = "Shiva",21,city="Hyd")''' #This raises a type error because it includes a positonal argument too.