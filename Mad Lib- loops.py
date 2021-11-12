# Mad Lib- Loop
# Write a program that takes a string and an integer as input, and outputs a sentence using the input
# values as shown in the example below. The program repeats until the input string is quit and disregards the
# integer input that follows.


user_input = input("Enter in a string and an integer:")
tokens = user_input.split()

while tokens[0] != "quit":
    if len(tokens) == 1:
        print('You need to input two values. A string and an integer.\n')
        user_input = input("Enter in a string and an integer:")
        tokens = user_input.split()
    else:
        print(f'Eating {tokens[1]} {tokens[0]} a day keeps the doctor away.\n\n'
              f'Enter in a string and an integer or type quit to stop:')
        user_input = input()
        tokens = user_input.split()
