import time
from codecs import lookup


def fib_rec(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_memo(n: int) -> int:
    if n <= 1:
        lookup[n] = n
    if lookup[n] is None:
        lookup[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return lookup[n]


n = 30
s = time.perf_counter()
print(fib_rec(n))
e = time.perf_counter()
print(e - s)
lookup = [None] * (n + 1)
s = time.perf_counter()
print(fib_memo(n))
e = time.perf_counter()
print(e - s)
