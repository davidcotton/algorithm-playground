"""Find all factors of a number."""

import math
from time import time
import timeit
from functools import reduce


def factors_naive(n):
    """A naive/brute-force solution for summing a numbers factors.
    
    Loop through all numbers between 1 and n searching for factors.
    """
    return {x for x in range(1, n + 1) if n % x == 0}


def factors_improved(n):
    """An improved method for summing the factors of a number.
    
    All factors of a number are paired, e.g. 6 has factors (1, 6) & (2, 3)
    
    We can reduce the search space by searching up to sqrt(n).
    
    We can assume that 1 & n will always be factors (n != 1) 
    to reduce our search between 2 & sqrt(n).
    """
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


def factors_double_improved(n):
    # trivial case
    if n == 1:
        return {1}

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


def time_method(fn, n):
    """Time how long each method takes."""
    return '{} took {}'.format(
        fn.__name__,
        timeit.timeit(
            '{}({})'.format(fn.__name__, n),
            setup='from __main__ import {}'.format(fn.__name__),
            number=3
        )
    )


def find_broken_methods(n, good_fn, dubious_fn):
    """Test helper for debugging."""
    for i in range(1, n + 1):
        good = good_fn(i)
        dubious = dubious_fn(i)
        if good != dubious:
            print('number: {}\n  good:    {}\n  dubious: {}'.format(i, sorted(good), sorted(dubious)))


if __name__ == '__main__':
    # find_broken_methods(100, factors_naive, factors_1)

    num = 12345678
    print(time_method(factors_naive, num))
    print(time_method(factors_improved, num))
    print(time_method(factors_double_improved, num))
