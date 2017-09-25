import math

from time_method import time_method_pp


def is_prime_naive(n):
    """Naive primality test.
    Loop through numbers from 2 to n and check if it is wholly divisible."""
    # trivial case
    if n <= 1:
        return False
    if n == 2:
        return True

    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def is_prime_noeven(n):
    """Improved primality test.
    No need to test all even numbers, if a number is not wholly divisible by 2,
    then it won't be divisible by multiples of 2."""
    # trivial case
    if n <= 1:
        return False
    if n == 2:
        return True

    # check even numbers
    if n % 2 == 0:
        return False

    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True


def is_prime_maxsqrt(n):
    """Optimised primality test.
    Only test numbers between 2 and square root of n (m).
    This is because to be a factor, a number must have a corresponding factor,
    where one side will be less than the square root of n."""
    # trivial case
    if n <= 1:
        return False
    if n == 2:
        return True

    m = int(math.sqrt(n))
    for i in range(3, m):
        if n % i == 0:
            return False
    return True


def is_prime_noeven_maxsqrt(n):
    """Optimised primality test.
    Only test numbers between 2 and square root of n (m).
    This is because to be a factor, a number must have a corresponding factor,
    where one side will be less than the square root of n."""
    # trivial case
    if n <= 1:
        return False
    if n == 2:
        return True

    # check even numbers
    if n % 2 == 0:
        return False

    m = int(math.sqrt(n))
    for i in range(3, m, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    # a few largish primes to test a full loop
    num = 1299709
    # num = 15485863
    # num = 179424673

    print(time_method_pp(is_prime_naive, num))
    print(time_method_pp(is_prime_noeven, num))
    print(time_method_pp(is_prime_maxsqrt, num))
    print(time_method_pp(is_prime_noeven_maxsqrt, num))