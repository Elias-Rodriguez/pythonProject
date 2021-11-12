# TODO: Import the random module
import random


def number_guess(num):
    # TODO: Get a random number between 1-100
    rnum = random.randint(1, 100)

    # TODO: Read numbers and compare to random number
    gnum = num
    if gnum > rnum:
        print("{} is too high. Random number was {}.".format(gnum, rnum))
    elif gnum < rnum:
        print("{} is too low. Random number was {}.".format(gnum, rnum))
    else:
        print("{} is correct!".format(gnum))


if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)

    # Convert the string tokens into integers
    user_input = input("Input your four guesses: ")
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)