# References to babylonian method below
# https://www.codespeedy.com/babylonian-method-to-find-square-root-using-python/#:~:text=The%20Babylonian%20method%20in%20Python%20This%20method%20follows,also%20initialize%20another%20variable%20%28say%20y%29%20to%201.
#

import math
def square_root(num):
    last_guess = int(num)
    next_guess = 1
    difference = 0.0001
    while last_guess - next_guess > difference:
        last_guess = (last_guess + next_guess )/2
        next_guess = num/last_guess
    return last_guess

# Custom function
print("Using the custom square root funtion.")
print("The square root of the number 15 is " + str(square_root(15)))

# Integrated math function

print("Using the imported square root funtion.")
print("The square root of the number 15 is " + str(math.sqrt(15)))