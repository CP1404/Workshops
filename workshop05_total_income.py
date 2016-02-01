"""
CP1404/CP5632 Workshop 05
Starter code for cumulative total income program
"""
__author__ = 'Lindsay Ward'

incomes = []
months = int(input("How many months? "))

for month in range(1, months + 1):
    income = float(input("Enter income for month " + str(month) + ": "))
    incomes.append(income)

print("\nIncome Report\n-------------")

total = 0
for month in range(1, months + 1):
    income = incomes[month - 1]
    total += income
    print("Month {:2d} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
