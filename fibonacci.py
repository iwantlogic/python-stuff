from functools import wraps
from time import perf_counter
import sys
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@memoize
def fibo(n):
    if n < 2:
        return n
    value = fibo(n - 1) + fibo(n - 2)
    return value
sys.setrecursionlimit(100_000)
start = perf_counter()
print(start)
print(fibo(int(input())))
end = perf_counter()
print(end)
print(f"{end-start}")
