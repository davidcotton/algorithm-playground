"""Insertion sort.
"""


class InsertionSort:
    """
        Insertion Sort
        --------------

        Time Complexity:
          - Best: O(n)
          - Avg: O(n^2)
          - Worst: O(n^2)

        Space Complexity:
          - O(n)
    """

    @staticmethod
    def sort(l):
        for i in range(1, len(l)):
            temp = l[i]
            j = i - 1
            while j >= 0 and l[j] > temp:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = temp
        return l


if __name__ == '__main__':
    data = [4, 2, 8, 6, 0, 5, 1, 7, 3, 9]
    print(InsertionSort().sort(data))
