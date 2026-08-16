def itemBillCal(*items):
    print("Items in the bill are: ", items) #returns the items in the bill in tuple format
    print("Total bill amount is: ", sum(items))
itemBillCal(100, 200, 300, 400, 500)
