"""Dynamic programming examples with the Fibonacci Sequence.
Calculate the sequence value at a particular index."""

import argparse
import matplotlib.pyplot as plt
import sys
from time_method import time_method


def recursive(n):
    if n < 2:
        return 1
    return recursive(n - 1) + recursive(n - 2)


def dynamic_programming(n):
    fib: list = [None] * (n + 1)
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, default=500, help='The fibonacci sequence index to calculate to')
    parser.add_argument('--verbose', help='Verbose output', action='store_true')
    args = parser.parse_args()
    steps = args.steps
    verbose = args.verbose
    results = {'recursive': [], 'dynamic_programming': []}
    to_skip = []
    module = sys.modules[__name__]
    time = 0
    result = 0
    for i in range(3, steps + 1):
        try:
            for fn in results.keys():
                if fn not in to_skip:
                    _, time, result = time_method(getattr(module, fn), i)
                    results[fn].append(time)
                if time > 10:
                    print(f'skipping {fn} with time {time:.4f}')
                    to_skip.append(fn)
        except AttributeError:
            print(f'Method {fn} does not exist')
            break
        if verbose:
            print(f'{i}: {result}')

    print(f'final iteration time {time:.5f}')
    plt.title('Fibonacci Sequence Performance')
    for name, values in results.items():
        plt.plot(values)
    plt.ylabel('time (seconds)')
    plt.xlabel('steps')
    plt.legend(results.keys(), loc='upper left')
    plt.show()
