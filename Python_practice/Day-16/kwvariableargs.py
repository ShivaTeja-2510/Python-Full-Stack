#keyword variable-length arguments
def printDetails(**details):
    print("Details of the user are: ", details) #returns the details of the user in dictionary format
    for key, value in details.items():
        print(key, ":", value)

printDetails(name="Shiva Teja", age=21, city="Hyderabad")