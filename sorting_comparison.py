"""Sort data using various algorithms."""

from bubble_sort import BubbleSort
from bucket_sort import BucketSort
from heap_sort import HeapSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from radix_sort import RadixSort
from selection_sort import SelectionSort
from copy import deepcopy
import os.path
from statistics import median
from time import time

NUM_SORTS = 1
PRECISION = 5
DEBUG_MODE = True


def read_file(f):
    """Read in a file to sort."""
    f = os.path.join(os.path.dirname(__file__), f)
    if not os.path.isfile(f):
        raise FileNotFoundError('Could not find "{}"'.format(f))
    with open(f, 'r') as file:
        result = [int(line) for line in file]
    return result


def run_sort(sorter, data):
    """Run a sorting algorithm and time the sorting."""
    times = []
    data2 = []
    for i in range(NUM_SORTS):
        data2 = deepcopy(data)
        t0 = time()
        sorter.sort(data2)
        times.append(time() - t0)

    print(sorter.__class__.__name__)
    print('---------------')
    if DEBUG_MODE:
        # check the list is sorted
        if not all(b >= a for a, b in zip(data2, data2[1:])):
            print('Not sorted\n  {}...\n  {}...\n'.format(data[0:20], data2[0:20]))
    # median
    print('  Median time: {}s'.format(round(median(times), PRECISION)))

    # remove highest & lowest times (to account for warm-up time)
    if len(times) > 4:
        times.remove(max(times))
        times.remove(min(times))
    avg = sum(times) / len(times)
    print('  Avg time: {}s\n'.format(round(avg, PRECISION)))


if __name__ == '__main__':
    d = read_file('./data/integers/100.txt')
    run_sort(BubbleSort(), d)
    run_sort(InsertionSort(), d)
    run_sort(SelectionSort(), d)
    run_sort(HeapSort(), d)
    run_sort(MergeSort(), d)
    # run_sort(QuickSort(), d)
    run_sort(RadixSort(), d)
    run_sort(BucketSort(), d)
