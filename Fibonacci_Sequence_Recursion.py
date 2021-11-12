# The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the
# previous two, for example: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which takes
# in an index, n, and returns the nth value in the sequence. Any negative index values should return -1.

def fibonacci(n):
    if n < 0:
        return -1
    elif n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    start_num = int(input("Type in the index you would like the value of:"))
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))


