for i in range(0,5):
    units = int(input("Enter the number of units consumed: "))
    if units <= 100:
        total = units*10
    elif units > 100 and units<=200:
        total = 100*10 + (units-100)*15
    elif units > 200:
        total = 100*10 + 100*15 + (units-200)*20
    print("Total electricity bill: ", total)