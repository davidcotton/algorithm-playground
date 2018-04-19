"""Minimum Steps to One.
On a positive integer, you can perform any one of the following 3 steps.
  1.) Subtract 1 from it. ( n = n - 1 ),
  2.) If its divisible by 2, divide by 2. (if n % 2 == 0, then n = n / 2),
  3.) If its divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3).
Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1
"""

import argparse
from time_method import time_method_pp


def memoization(n):
    pass


def bottom_up(n):
    dp: list = [None] * (n + 1)
    dp[1] = 0  # trivial case
    for i in range(2, n + 1):
        dp[i] = 1 + dp[i - 1]
        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + dp[int(i / 2)])
        if i % 3 == 0:
            dp[i] = min(dp[i], 1 + dp[int(i / 3)])
    return dp[n]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, default=9, help='The number to start from')
    args = parser.parse_args()
    start = args.start
    print('Bottom up steps: {}'.format(bottom_up(start)))
    # print('Memoization steps: {}'.format(memoization(start)))
