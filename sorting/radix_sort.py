"""
Radix sort is a non-comparative, integer sorting algorithm.
"""


class RadixSort:
    """
        Radix Sort
        ----------

        Time Complexity:
          - Best: O(wn)
          - Avg: O(wn)
          - Worst: O(wn)

        Space Complexity:
          - O(w + N)
    """

    @staticmethod
    def sort(data):
        num_digits = max(data)
        exp = 1
        while num_digits / exp > 0:
            RadixSort.bucket_sort(data, exp)
            exp *= 10

    @staticmethod
    def bucket_sort(data, exp):
        n = len(data)
        result = [0] * n
        count = [0] * 10
        for i in range(0, n):
            index = data[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= n:
            index = data[i] // exp
            result[count[index % 10] - 1] = data[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, n):
            data[i] = result[i]


if __name__ == '__main__':
    l = [4, 2, 8, 6, 0, 5, 1, 7, 3, 9]
    RadixSort().sort(l)
    print(l)
