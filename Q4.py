initial_balance = 50000
successful_withdrawals = 0

while initial_balance > 0:
    amount = int(input("Enter the amount to withdraw: "))
    
    if amount == -1:
        break
    elif amount > initial_balance:
        print("Insufficient balance.")
    elif amount <= 0:
        print("Invalid amount.")
    else:
        initial_balance = initial_balance - amount
        successful_withdrawals = successful_withdrawals + 1

print("Remaining balance:", initial_balance)
print("Total amount withdrawn:", 50000 - initial_balance)
print("Total number of successful withdrawals:", successful_withdrawals)