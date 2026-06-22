Total = 0
items = 0
while True:
    price = int(input("Enter the price: "))
    if price ==  0:
        break
    else:
        Total = Total + price
        items = items + 1
print("Total bill amount is: ", Total)
print("Number of items: ", items)
print("Average price per item: ", Total/items)