"""Find all factors of a number."""

import math
from time_method import time_method


def factors_naive(n):
    """A naive/brute-force solution for summing a numbers factors.
    
    Loop through all numbers between 1 and n searching for factors."""
    return {x for x in range(1, n + 1) if n % x == 0}


def factors_maxsqrt(n):
    """An improved method for summing the factors of a number.
    
    All factors of a number are paired, e.g. 6 has factors (1, 6) & (2, 3)
    
    We can reduce the search space by searching up to sqrt(n).
    
    We can assume that 1 & n will always be factors (n != 1) 
    to reduce our search between 2 & sqrt(n)."""
    # trivial case
    if n == 1:
        return {1}

    max_d = int(math.sqrt(n))
    factors = {1, n}
    for i in range(2, max_d + 1):
        if n % i == 0:
            factors.add(i)
            d = n // i
            if d != i:
                factors.add(d)
    return factors


def factors_noeven_maxsqrt(n):
    """Improved the less than square root method for even numbers."""
    # trivial case
    if n == 1:
        return {1}

    # use a step for even numbers
    step = 2 if n % 2 == 0 else 1
    factors = {1, n}
    max_d = int(math.sqrt(n))
    for i in range(2, max_d + 1, step):
        if n % i == 0:
            factors.add(i)
            d = n // i
            if d != i:
                factors.add(d)
    return factors


def find_broken_methods(n, good_fn, dubious_fn):
    """Test helper for debugging."""
    for i in range(1, n + 1):
        good = good_fn(i)
        dubious = dubious_fn(i)
        if good != dubious:
            print('number: {}\n  good:    {}\n  dubious: {}'.format(i, sorted(good), sorted(dubious)))


if __name__ == '__main__':
    # find_broken_methods(100, factors_naive, factors_1)

    num = 123456789
    print(time_method(factors_naive, num))
    print(time_method(factors_maxsqrt, num))
    print(time_method(factors_noeven_maxsqrt, num))
