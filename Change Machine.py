# Programming Exam: Use the cashier's algorithm. Develop a program that randomly selects a total charge. Then
# randomly select a payment in dollars and cents that exceeds that charge. Then have the program calculate the change
# in pennies, nickels, dimes, quarters, ones, fives, tens, and twenties.

import random

# variables for generating values
amount_charged = round(random.uniform(1, 20), 2)
amount_given = round(random.uniform(amount_charged, 50), 2)
change: float = round((-amount_charged + amount_given), 2)

# variable to hold the initial change value
change_u = change

# Variables to hold the amount of each bill or coin
bill_twenty = 0
bill_ten = 0
bill_five = 0
bill_one = 0
quarter = 0
dime = 0
nickel = 0
penny = 0

# Looping statement to generate amount of each bill or coin needed to obtain change
while change != 0:
    if change < .05:
        penny = int(change / .009)
        change = 0
    elif change < .10:
        nickel = int(change / .05)
        change = round((change - (nickel * .05)), 2)
    elif change < .25:
        dime = int(change / .10)
        change = round((change - (dime * .10)), 2)
    elif change < 1:
        quarter = int(change / .25)
        change = round((change - (quarter * .25)), 2)
    elif change < 5:
        bill_one = int(change / 1)
        change = change - bill_one
    elif change < 10:
        bill_five = int(change / 5)
        change = change - (bill_five * 5)
    elif change < 20:
        bill_ten = int(change / 10)
        change = change - (bill_ten * 10)
    elif change > 20:
        bill_twenty = int(change / 20)
        change = change - (bill_twenty * 20)


# Print in order to see if the amounts are correct.
print('The amount charged was {}.\n The amount the user paid with was {}.\n '
      'The change given back was {} in the amount of {} twenty dollar bill(s), {} ten dollar bill(s), '
      '{} five dollar bill(s), {} one dollar bill(s), {} quarter(s), {} dime(s),'
      ' {} nickel(s), and {} penny/pennies.'.format(amount_charged, amount_given, change_u, bill_twenty, bill_ten,
                                                  bill_five, bill_one,
                                                  quarter, dime, nickel, penny))
