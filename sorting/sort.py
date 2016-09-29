"""Sort data using various algorithms."""

from bubble_sort import BubbleSort
from heap_sort import HeapSort
from insertion_sort import InsertionSort
from quick_sort import QuickSort
from merge_sort import MergeSort, MergeSortStrict
from copy import deepcopy
import os.path
from statistics import median
from time import time

NUM_SORTS = 1
DIGITS = 3


def read_file(f):
    """Read in a file to sort."""
    result = []
    if not os.path.isfile(f):
        return result

    with open(f, 'r') as file:
        for line in file:
            result.append(int(line))
    return result


def run_sort(sorter, data):
    """Run a sorting algorithm and time the sorting."""
    times = []
    for i in range(NUM_SORTS):
        t0 = time()
        d2 = deepcopy(data)
        sorter.sort(d2)
        times.append(time() - t0)
        # print(data[0:20])
        # print(d2[0:20])

    print(sorter.__class__.__name__)
    # median
    print('Median time: {}s'.format(round(median(times), DIGITS)))

    # remove highest & lowest times
    if len(times) > 4:
        times.remove(max(times))
        times.remove(min(times))
    avg = sum(times) / len(times)
    print('Avg time: {}s\n'.format(round(avg, DIGITS)))


if __name__ == '__main__':
    d = read_file('../data/10000000.txt')
    # run_sort(BubbleSort(), d)
    # run_sort(InsertionSort(), d)
    # run_sort(HeapSort(), d)
    run_sort(MergeSort(), d)
    run_sort(MergeSortStrict(), d)