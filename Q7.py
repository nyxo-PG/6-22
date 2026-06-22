sales_list = []

for i in range(1, 8):
    sales = float(input(f"Enter the sales amount for Day {i}: "))
    sales_list.append(sales)

total_sales = sum(sales_list)
average_sales = total_sales / 7
highest_sales = max(sales_list)
lowest_sales = min(sales_list)

print("\n--- Product Sales Report ---")
print(f"Total weekly sales: {total_sales:.2f}")
print(f"Average daily sales: {average_sales:.2f}")
print(f"Highest sales amount: {highest_sales:.2f}")
print(f"Lowest sales amount: {lowest_sales:.2f}")