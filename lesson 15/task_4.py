results = []
sales = input("Enter 3 managers sells divided by spaces, ex: '100 300 500': ").split()
for employee_sales in sales:
    if float(employee_sales) < 500:
        income = 200 + float(employee_sales) * 0.03
        results.append(income)
    elif float(employee_sales) >= 500 and float(employee_sales) <= 1000:
        income = 200 + float(employee_sales) * 0.05
        results.append(income)
    elif float(employee_sales) > 1000:
        income = 200 + float(employee_sales) * 0.08
        results.append(income)
    elif float(employee_sales) < 0:
        print("Stop kidding, you can't have negative sales!")
        break
best_inc = max(results)
best_emp = results.index(best_inc)
results[best_emp] += 200
print(f"\nThe best manager is {best_emp + 1}!")
print("\nManagers have following incomes: ")
for emp in results:
    print(f"\t{results.index(emp) + 1} - {emp} $!")
