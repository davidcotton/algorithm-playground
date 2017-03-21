"""
Generate text files with random numbers to sort.
"""


from argparse import ArgumentParser
from random import randint


MAX_INT = 1000000
NUM_INT = 10000000
DATA_DIR = 'integers'


def gen_integers(n, max_n):
    """Generate and write random numbers to a file"""
    file = open('{}/{}.txt'.format(DATA_DIR, n), 'w')
    for i in range(n):
        line = '{}\n'.format(str(randint(1, max_n)))
        file.write(line)
    file.close()


def gen_dna(n):
    file = open('{}/dna-{}.txt'.format(DATA_DIR, n), 'w')
    file.close()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-n", help="The number of integers to generate", type=int)
    parser.add_argument("--max", help="The maximum integer to generate", type=int)
    args = parser.parse_args()
    gen_integers(
        args.n if args.n else NUM_INT,
        args.max if args.max else MAX_INT
    )
