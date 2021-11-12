# Palindrome
# A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are:
# "bob," "sees," or "never odd or even" (ignoring spaces).
# Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

user_input = input("Type in a word or a phrase to see if its a palindrome:")

normal_str = user_input.replace(" ", "")
reverse_str = normal_str[::-1]

if normal_str == reverse_str:
    print('{} is a palindrome'.format(user_input))
else:
    print('{} is not a palindrome'.format(user_input))