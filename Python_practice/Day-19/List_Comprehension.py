'''
Syntax: 
1. [expression for var in sequence]
2. [expression for var in sequence condition]
'''

# Examples for List Comprehensions
# Printing 1 to 5 using list comprehensions
l1=[i for i in range(1,6)]
print("Example-1 Result: ",l1)

# Printing squares from 1 to 5 numbers
l2=[i*i for i in range(1,6)]
print("Example-2 Result: ",l2)

# Printing even no.s between 1 and 10
l3=[i for i in range(1,11) if i%2==0]
print("Example-3 Result: ",l3)

# Uppercase a list of strings
names=["shiva",'teju','pranavi']
l4=[i.upper() for i in names]
print("Example-4 Result: ",l4)

# Prices greater than 2000
prices=[8000,2444,5000,8000,1000]
l5=[i for i in prices if i>2000]
print("Example-5 Result: ",l5)

# Printing the index of empty stocks in the market
stocks=[1,3,0,9,10,0]
l6=[index for index,val in enumerate(stocks) if val==0] #not val
print("Example-6 Result: ",l6)

# Using the List Comprehensions using in the nested collections
products=[('laptop',50000),('mobile',40000),('tab',30000)]
# Display the products where price > 30000
l7=[product[0] for product in products if product[1]>30000]
print("Example-7 Result: ",l7)

# Incase of a dictionary
pinfo = [{'name':'laptop','price':50000,'stock':2},
         {'name':'mobile','price':30000,'stock':0},
         {'name':'tab','price':10000,'stock':6}]
l8=[i['name'] for i in pinfo if i['stock']>0]
print("Example-8 Result: ",l8)



