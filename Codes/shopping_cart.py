item = input("What items would you like to buy ? :")
price = float(input("what is the price of the item ? :"))
quantity = int(input("hoiw many would you like ? :"))

print(f"The item is :{item}")
print(f"The price is : {price}")
print(f"Quantity is  : {quantity}")
total = price *quantity
print(f"The Total amout is : ${round(total,2)}")   #round is used to reduce the number of decimal parts
print(f"You have brought {quantity} x {item}/s ")
