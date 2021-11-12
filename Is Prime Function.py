# Is Prime function
# Resources: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#:~:text=To%20find%20all%20the%20prime%20numbers%20less%20than,let%20p%20equal%202%2C%20the%20smallest%20prime%20number.
#

import math


def prime_less_than(n):
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    number = math.sqrt(n)
    number = round(number)+1
    for i in range(2, number):
        if is_prime[i]:
            for x in range(i * i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]

print("We are about to test how many numbers are prime that are less than the user given input.")
user_num = int(input("What number would you like to use:\n"))
print("Currently testing to see how many numbers are prime that are less than" , user_num)
list_of_prime_numbers = prime_less_than(user_num)
amount_of_prime_numbers = len(list_of_prime_numbers)
print("There are {} prime numbers less than {}".format(amount_of_prime_numbers,user_num))
print("Printing out the numbers found.")
#print(list_of_prime_numbers)
