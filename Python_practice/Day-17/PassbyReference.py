def update(items):
    print("Inside the function:",items)
    items.append("Laptop")
cart = ["Mobile", "Watch"]
update(cart)
print("After Updating:",cart)