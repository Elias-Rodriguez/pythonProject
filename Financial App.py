# Financial App: Compute future investment value
# Resources: https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
#


import math


def financial_application(initial_value, rate, years):
    future_val = (initial_value * (1 + rate) ** (years * 12))
    print("The investment value after ", years, " years is ", round(future_val, 2))


financial_application(10000, 0.05 / 12, 5)


