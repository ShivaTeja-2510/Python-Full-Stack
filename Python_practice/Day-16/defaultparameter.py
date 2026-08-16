#Using the default parameter

def userDetails(name, age=21, city="Hyderabad"):
    print("Hello I am", name, "! I am", age, "years old and I live in", city)

# Calling the function with different combinations of arguments
userDetails("Shiva Teja")  # Uses default values for age and city
userDetails("Varun", 25)   # Uses default value for city
userDetails("Nishanth", 30, "Bangalore")  # Uses all provided values


