"""
    Bucket sort is a comparative sorting algorithm that sorts elements into a number of buckets.
"""

from math import floor

from src.sorting.insertion_sort import InsertionSort


class BucketSort:
    """
        Bucket Sort
        ----------

        k = number of buckets

        Time Complexity:
          - Best: O(n + k)
          - Avg: O(n + k)
          - Worst: O(n^2) (when all elements are assigned to the same bucket)

        Space Complexity:
          - O(n + k)
    """
    BUCKET_SIZE = 10

    def sort(self, data):
        max_n = min_n = 0
        for i, x in enumerate(data):
            if x > max_n:
                max_n = x
            elif x < min_n:
                min_n = x

        # Initialise buckets
        num_buckets = self.get_bucket_size(min_n, max_n) + 1
        buckets = [[] for _ in range(num_buckets)]

        # Distribute input into buckets
        for i, x in enumerate(data):
            buckets[self.get_bucket_size(min_n, x)].append(x)

        # Sort buckets
        sorter = InsertionSort()
        result = []
        for i, b in enumerate(buckets):
            result += sorter.sort(b)

        return result

    def get_bucket_size(self, min_n, max_n) -> int:
        return int(floor((max_n - min_n) / self.BUCKET_SIZE))


if __name__ == '__main__':
    print(BucketSort().sort([20, 6, 12, 16, 4, 10, 2, 6, 16, 13]))
