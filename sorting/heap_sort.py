"""Heap sort.
"""


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

    @staticmethod
    def sort(l):
        return l


if __name__ == '__main__':
    data = [4, 2, 8, 6, 0, 5, 1, 7, 3, 9]
    print(HeapSort().sort(data))
