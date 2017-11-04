"""Heap sort is a comparison-based sorting algorithm.
Heap sort uses the "heap" data-structure
"""

from datastructures.heap import BinaryHeap


class HeapSort:
    """
        Heap Sort
        ----------

        Time Complexity:
          - Best: O(n log n)
          - Avg: O(n log n)
          - Worst: O(n log n)

        Space Complexity:
          - O(n)
    """
    def sort(self, data):
        heap = BinaryHeap()
        for d in data:
            heap.insert(d)

        result = []
        while not heap.empty():
            result.append(heap.remove_min())

        return result


if __name__ == '__main__':
    import random

    # print(HeapSort().sort([4, 2, 8, 6, 0, 5, 1, 7, 3, 9]))

    n = 20
    max_n = 1000
    data = [random.randint(1, max_n) for _ in range(n)]
    print(HeapSort().sort(data))
