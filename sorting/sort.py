"""Sort data using various algorithms."""

from bubble_sort import BubbleSort
from bucket_sort import BucketSort
from heap_sort import HeapSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort, MergeSortStrict
from quick_sort import QuickSort
from radix_sort import RadixSort
from copy import deepcopy
import os.path
from statistics import median
from time import time

NUM_SORTS = 1
PRECISION = 3


def read_file(f):
    """Read in a file to sort."""
    result = []
    if not os.path.isfile(f):
        return result
    with open(f, 'r') as file:
        result = [int(line) for line in file]
    return result


def run_sort(sorter, data):
    """Run a sorting algorithm and time the sorting."""
    times = []
    for i in range(NUM_SORTS):
        d2 = deepcopy(data)
        t0 = time()
        sorter.sort(d2)
        times.append(time() - t0)
        # print(data[0:20])
        # print(d2[0:20])

    print(sorter.__class__.__name__)
    # median
    print('Median time: {}s'.format(round(median(times), PRECISION)))

    # remove highest & lowest times (to account for warm-up time)
    if len(times) > 4:
        times.remove(max(times))
        times.remove(min(times))
    avg = sum(times) / len(times)
    print('Avg time: {}s\n'.format(round(avg, PRECISION)))


if __name__ == '__main__':
    d = read_file('../data/1000000.txt')
    # run_sort(BubbleSort(), d)
    # run_sort(InsertionSort(), d)
    # run_sort(HeapSort(), d)
    # run_sort(MergeSort(), d)
    run_sort(MergeSortStrict(), d)
    # run_sort(QuickSort(), d)
    # run_sort(RadixSort(), d)
    run_sort(BucketSort(), d)
