# Login Name
# Write a program that creates a login name for a user, given the user's first name, last name, and a
# four-digit integer as input. Output the login name, which is made up of the first five letters of
# the last name, followed by the first letter of the first name, and then the last two digits of the
# number (use the % operator). If the last name has less than five letters, then use all letters of the last name.


values = input('Input your first name, last name, and a four digit number(ex: elias rodriguez 2021):').split()
first = values[0]
last = values[1]
number = int(values[2])

if len(last) > 5:
    last = last[:5]

print("Your login name: {}{}{}".format(last, first[0], number % 100))