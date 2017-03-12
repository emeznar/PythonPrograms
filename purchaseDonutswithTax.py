print ("""Welcome to the loop hole!
Today's Manager's special is:
Crunch jelly: A traditional jelly donut in which the jelly filling is made entirely of 
Capn' Crunch Berries Oops All Berries""")

quantity = float(input("How many would you like?"))
print(quantity)
price = float(input("How much would you like to pay per donut - suggested price is $4.35 each?"))
print (price)

print ("OK, let me prepare that for you.....")
tax = (quantity*price)*.05
answer = round(((quantity * price)+ tax), 2)

print ("Your total with tax is $",answer)