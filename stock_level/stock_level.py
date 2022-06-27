stock_level = int(input("Please enter an initial stock level: "))
plan_months = int(input("Please enter the number of months to plan: "))
planned_sales_quantity = []

for x in range(plan_months):
    planned_sales_quantity.append(int(input("Please enter the planned quantity: ")))

print("The resulting production quantities are:")

for index, sales in zip([x+1 for x in range(plan_months)], planned_sales_quantity):
    production_quantity = 0
    if sales < stock_level:
        print(f"Production quantity month {index} - : " + str(0))
    elif sales > stock_level:
        production_quantity = sales-stock_level
        print(f"Production quantity month {index} - : " + str(production_quantity))
    stock_level += production_quantity - sales