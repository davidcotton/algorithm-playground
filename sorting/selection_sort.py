"""
    Selection sort is an in place comparison sort.
    Selection sort divides the list into into two lists: one sorted and one to sort.
    The algorithm proceeds by finding the smallest element in the unsorted list
    and swapping it into the sorted list.
"""


class SelectionSort:
    """
        Selection Sort
        --------------

        Time Complexity:
          - Best: O(n^2)
          - Avg: O(n^2)
          - Worst: O(n^2)

        Space Complexity:
          - O(1)
    """

    @staticmethod
    def sort(l):
        for j in range(len(l)):
            i_min = j
            for i in range(j + 1, len(l)):
                if l[i] < l[i_min]:
                    i_min = i
            l[i_min], l[j] = l[j], l[i_min]
        return l


if __name__ == '__main__':
    data = [4, 2, 8, 6, 0, 5, 1, 7, 3, 9]
    print(SelectionSort().sort(data))
