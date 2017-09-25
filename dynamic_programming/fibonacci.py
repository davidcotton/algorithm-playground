"""Fibonacci"""

from time_method import time_method_pp


def recursive(n):
    if n < 2:
        return 1
    return recursive(n - 1) + recursive(n - 2)


def dynamic_programming(n):
    fib = [None] * (n + 1)
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


if __name__ == '__main__':
    n = 40
    print(time_method_pp(recursive, n))
    print(time_method_pp(dynamic_programming, n))
