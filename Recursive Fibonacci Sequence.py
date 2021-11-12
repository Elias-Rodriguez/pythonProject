import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


i = 1
tic = time.perf_counter()
while i <= 35:
    print(fibonacci(i))
    i += 1
toc = time.perf_counter()

print(f"second it took to calculate numbers 1 through 35 = {toc - tic:0.8f} seconds")
