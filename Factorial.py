# Function for Factorial

def factorial(number):
    total = 0
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


user_input = (int(input("Type in the number you like to know the factorial of:")))
print("{} factorial is {}".format(user_input, factorial(user_input)))