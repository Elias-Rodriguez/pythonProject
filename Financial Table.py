# Investment amount table
# Resources: https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
#

def financialAppTable(initialValue, rate):
    fValue = (initialValue * (1 + (rate * 0.01)/12) ** (i * 12))
    print("Year ", i, " is ", round(fValue, 2))


amount = float(input("Enter the investment amount: "))
rate = input("Enter the rate(ex: 8%):")
rate = rate.replace('%', '')
rate = float(rate)
for i in range(1, 31):
    financialAppTable(amount, rate)

