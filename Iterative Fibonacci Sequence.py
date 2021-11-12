import time


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


i = 1
tic = time.perf_counter()
while i <= 35:
    (fibonacci(i))
    i += 1
toc = time.perf_counter()

print(f"second it took to calculate numbers 1 through 35 = {toc - tic:0.8f} seconds")
