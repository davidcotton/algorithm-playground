"""Compare various pattern matching algorithms."""

import codecs
import os.path
from statistics import median
from time import time
from brute_force import BruteForce
from boyer_moore import BoyerMoore
from kmp import KMP
from trie import DefaultTrie

NUM_SORTS = 1
PRECISION = 5
DATA_DIR = '../corpora'


def read_file(f):
    """Read in a file to sort."""
    if not os.path.isfile(f):
        raise RuntimeError('File does not exist')
    result = ''
    f = codecs.open(f, encoding='utf-8')
    for line in f:
        result += ' {}'.format(line)
    return result


def get_file(f):
    return '{}/{}.txt'.format(DATA_DIR, f)


def run_search(matcher, pattern, text):
    """Run a text searching algorithm and time the searching."""
    times = []
    for i in range(NUM_SORTS):
        t0 = time()
        result = matcher.search(pattern, text)
        times.append(time() - t0)
        print('Result is {}'.format(result))

    print(matcher.__class__.__name__)
    # median
    print('  Median time: {}s'.format(round(median(times), PRECISION)))

    # remove highest & lowest times (to account for warm-up time)
    if len(times) > 4:
        times.remove(max(times))
        times.remove(min(times))
    avg = sum(times) / len(times)
    print('  Avg time: {}s\n'.format(round(avg, PRECISION)))


if __name__ == '__main__':
    p = 'pattern'
    # t = read_file(get_file('wikipedia_trie'))
    # t = read_file(get_file('sherlock'))
    t = read_file(get_file('big'))
    # t = read_file(get_file('super_big'))
    run_search(BruteForce(), p, t)
    run_search(BoyerMoore(), p, t)
    # run_search(KMP(), p, t)
    # run_search(Trie(), p, t)
