__author__ = 'sci-lmw1'

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def format_currency(value):
    return "$" + format(value, '.2f')

tariff_choice = input("Which tariff? 11 or 31: ")
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
if tariff_choice == "11":
    tariff_rate = TARIFF_11
else:
    tariff_rate = TARIFF_31
total_bill = tariff_rate * daily_use * billing_days

print("\nEstimated bill:", format_currency(total_bill))
