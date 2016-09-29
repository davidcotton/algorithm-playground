"""
Generate text files with random numbers to sort.
"""

from random import randint

MAX_INT = 100000000


def gen_random(n):
    """Generate and write random numbers to a file"""
    file = open('{}.txt'.format(n), 'w')
    for i in range(n):
        line = '{}\n'.format(str(randint(1, MAX_INT)))
        file.write(line)
    file.close()

gen_random(10000000)
