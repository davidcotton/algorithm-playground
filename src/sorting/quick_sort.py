"""
    Quick sort is an efficient, randomised, comparision sorting algorithm.
    Quick sort is a divide & conquer algorithm.
    Unlike merge sort the majority of the work in quick sort happens during the divide step.

    Quick sort works in place.
    In the worst case quick sort degrades to quadratic.
    In practice quick sort often outperforms merge sort as its constant operations
    are faster than merge sorts.
"""

from abc import ABC

from src.datastructures.stack import ArrayStack


class QuickSort(ABC):
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
    def partition(self, data, left, right):
        i = left - 1
        pivot = data[right]
        for j in range(left, right):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[right] = data[right], data[i + 1]
        return i + 1


class RecursiveQuickSort(QuickSort):
    """A recursive implementation of the quicksort algorithm."""
    def sort(self, data, left=0, right=None):
        if right is None:
            right = len(data) - 1
        if left < right:
            pivot = self.partition(data, left, right)
            data = self.sort(data, left, pivot - 1)
            data = self.sort(data, pivot + 1, right)
        return data


class IterativeQuickSort(QuickSort):
    """An iterative implementation of the quicksort algorithm."""
    def sort(self, data):
        # trivially sorted
        if len(data) < 2:
            return data

        stack = ArrayStack((0, len(data) - 1))
        while not stack.is_empty():
            left, right = stack.pop()
            pivot = self.partition(data, left, right)

            if pivot - 1 > left:
                stack.push((left, pivot - 1))

            if pivot + 1 < right:
                stack.push((pivot + 1, right))

        return data


if __name__ == '__main__':
    l = [4, 2, 8, 6, 0, 5, 1, 7, 3, 9]
    print('RecursiveQuickSort: {}'.format(RecursiveQuickSort().sort(list(l))))
    print('IterativeQuickSort: {}'.format(IterativeQuickSort().sort(list(l))))
