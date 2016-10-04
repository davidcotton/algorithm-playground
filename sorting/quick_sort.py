"""
    Quick sort is an efficient, randomised, comparision sorting algorithm.
    Quick sort is a divide & conquer algorithm.
    Unlike merge sort the majority of the work in quick sort happens during the divide step.

    Quick sort works in place.
    In the worst case quick sort degrades to quadratic.
    In practice quick sort often outperforms merge sort as its constant operations
    are faster than merge sorts.
"""


class QuickSort:
    """
        Quick Sort
        ----------

        w = word length

        Time Complexity:
          - Best: O(n log n)
          - Avg: O(n log n)
          - Worst: O(n^2)

        Space Complexity:
          - O(n)
    """

    @staticmethod
    def sort(data, low=0, high=None):
        if high is None:
            high = len(data) - 1
        if low < high:
            pivot = QuickSort.partition(data, low, high)
            data = QuickSort.sort(data, low, pivot - 1)
            data = QuickSort.sort(data, pivot, high)
        return data

    @staticmethod
    def partition(data, low, high):
        i = low - 1
        pivot = data[high]
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1


if __name__ == '__main__':
    l = [4, 2, 8, 6, 0, 5, 1, 7, 3, 9]
    print(QuickSort().sort(l))
