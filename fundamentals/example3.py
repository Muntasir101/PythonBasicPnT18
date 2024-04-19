"""
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
"""
unit_price = 100
quantity = int(input("Enter quantity: "))
initial_price = quantity * unit_price

if initial_price > 1000:
    discount = initial_price * .1
    print("Initial Cost: ", initial_price)
    print("Your discount Amount: ", discount)
    print("After Discount Cost is: ", (initial_price - discount))
else:
    print("No Discount.Cost is: ", quantity * 100)
